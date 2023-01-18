import os
import uuid
import requests
from app.services.requests.params import custom_parameters
from app.services.user.relationship import create_user_institutions, create_user_secretaries
from app.services.utils import code_generator

from flask import request
from sqlalchemy import or_

from app import models, schemas
from app.controllers import CRUDBase, crud_user_address
from app.services.errors.exceptions import GenerateError, NotFoundError, UnauthorizedError
from app.services.security.password import get_password_hash


class CRUDUser(CRUDBase):

    def list_users(self):
        """
        It gets the data from the database, filters it, paginates it, and returns it

        :param schema: The schema to be used to serialize the data
        :param columns: list of columns to be returned
        :param extra_filters: {'id': 1}
        :param active_order: Boolean
        :return: A tuple with two elements.
        """
        page, per_page, search, order, order_by = custom_parameters()
        group_id = request.args.get('group_id')
        institution_id = request.args.get('institution_id')

        query = self.class_model.query.filter(
            self.class_model.deleted_at.is_(None))

        if search:
            query = query.filter(
                or_(self.class_model.name.like(f'%%{search}%%')))

        if group_id:
            query = query.filter(self.class_model.group_id == group_id)

        if institution_id:
            query = query.join(
                models.UserInstitution, models.UserInstitution.user_id == self.class_model.id
            ).filter(
                models.UserInstitution.institution_id == institution_id,
                models.UserInstitution.deleted_at.is_(None)
            )

        column_sorted = getattr(getattr(self.class_model, order),
                                order_by)()
        query = query.order_by(column_sorted)

        items = query.paginate(page, per_page, False)
        items_paginate = items

        items = self.class_schema(many=True).dump(items.items)

        return items, items_paginate

    def get_user_with_exist(self, email, taxpayer=False):

        query = self.class_model.query

        if taxpayer:
            query = query.filter(
                or_(self.class_model.email == email,
                    self.class_model.taxpayer == taxpayer))
            msg = "Já existe usuário com este email ou cpf"
        else:
            query = query.filter(self.class_model.email == email)
            msg = "Já existe usuário com este email"

        item = query.first()

        if item:
            raise GenerateError(status_code=409, error=msg)

    def create_user_with_exist(self, schema, exist_taxpayer=False,
                               specific_group_id=False):
        """
        It creates a user and validates the payment

        :param specific_group_id: Set specific user id
        :param exist_taxpayer: Validate identification document
        :param schema: The schema to use for validation
        :return: The return is a string, but I need to return the item.
        """
        dict_body = request.get_json()
        if 'address' in dict_body:
            dict_address = dict_body['address']
            del dict_body['address']

        # verify exist
        if exist_taxpayer and ('taxpayer' in dict_body):
            self.get_user_with_exist(dict_body['email'], dict_body['taxpayer'])
        else:
            self.get_user_with_exist(dict_body['email'])

        # add hash_id and hash in password
        if 'password' in dict_body:
            password = dict_body['password']
        else:
            password = code_generator(8)
        extra_fields = [("hash_id", str(uuid.uuid4())),
                        ("password", get_password_hash(password))]

        # specific group id
        if specific_group_id:
            extra_fields.append(("group_id", specific_group_id))

        item = self.post(dict_body=dict_body, extra_fields=extra_fields)

        if 'address' in dict_body:
            dict_address['user_id'] = item.id
            crud_user_address.post(dict_body=dict_address)
            
        create_user_institutions(item, dict_body)
        create_user_secretaries(item, dict_body)
        if schema:
            item = self.class_schema().dump(item)

        return item

    def get_user_by_jwt(self, user_jwt, schema=None):
        """
        It returns the first user that matches the hash_id in the user_jwt, has a status of 1, and has a
        deleted_at of None

        :param user_jwt: The JWT token that is passed in the header
        :return: A user object
        """
        item = self.class_model.query.filter(
            self.class_model.hash_id == user_jwt['hash_id'],
            self.class_model.status.is_(True),
            self.class_model.deleted_at.is_(None)).first()

        if schema:
            item = self.class_schema().dump(item)

        return item

    def validate_auth_request(self, username, basic):
        query = self.class_model.query.filter(
            self.class_model.status.is_(True),
            self.class_model.deleted_at.is_(None))

        if basic == os.environ.get("ADMIN_BASIC"):
            query = query.filter(self.class_model.group_id.not_in([5]))
        elif basic != os.environ.get("CLIENT_BASIC"):
            raise UnauthorizedError("Invalid Basic Negado")

        if "@" in username:
            query = query.filter(self.class_model.email == username)
        else:
            query = query.filter(self.class_model.cpf == username)

        user = query.first()

        return user

    def update_user_address(self, item_id):
        dict_body = request.get_json()['address']
        address = models.UserAddress.query.filter_by(id=item_id).first()
        if address:
            if "city_id" in dict_body:
                city = models.City.query.filter(
                    models.City.id == dict_body["city_id"]).first()
                if city is None:
                    raise NotFoundError("Cidade não encontrada")

            item = address.update(**dict_body)
            item = self.class_schema().dump(item)
            return item
        else:
            return None

    def update_user(self, item_id):
        dict_body = request.get_json()
        if 'email' in dict_body:
            del dict_body['email']

        item = self.put(item_id, dict_body=dict_body)

        if 'address' in dict_body:
            if item.address:
                self.update_user_address(item.address.id)

        create_user_institutions(item, dict_body)
        create_user_secretaries(item, dict_body)
        item = self.get(item_id)
        item = self.class_schema().dump(item)

        return item

    def find_cep(self):
        code_post = request.args.get('code_post')

        if code_post is None:
            raise NotFoundError('CEP não encontrado')

        header = {
            'Content-Type': 'application/json'
        }

        try:
            url = 'https://viacep.com.br/ws/{}/json/'.format(code_post)
            r = requests.get(url, headers=header)
            address = r.json()

            city_name = address['localidade']
            uf_name = address['uf']
            street = address['logradouro']
            district = address['bairro']
        except:
            try:
                url = 'http://cep.republicavirtual.com.br/web_cep.php?cep={}&formato=jsonp'.format(
                    code_post)
                r = requests.get(url, headers=header)
                address = r.json()

                city_name = address['cidade']
                uf_name = address['uf']
                street = f"{address['tipo_logradouro']} {address['logradouro']}"
                district = address['bairro']
            except:
                url = 'http://apps.widenet.com.br/busca-cep/api/cep/{}.json'.format(
                    code_post)
                r = requests.get(url, headers=header)
                address = r.json()

                city_name = address['city']
                uf_name = address['state']
                street = address['address']
                district = address['district']

        if uf_name == "":
            raise NotFoundError('Cidade não encontrada')

        city = models.City.query \
            .join(models.State, models.State.id == models.City.state_id) \
            .filter(models.City.name == city_name, models.State.uf == uf_name, models.City.deleted_at == None).first()

        return {
            "code_post": code_post,
            "street": street,
            "number": "",
            "district": district,
            "complement": '',
            "city": schemas.CitySchema().dump(city)
        }


# Creating an instance of the class CRUDUser.
crud_user = CRUDUser(models.User, schemas.UserSchema)
