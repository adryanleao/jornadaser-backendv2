
from flask import request

from app import models, schemas
from app.controllers import (CRUDBase, crud_secretary_address,
                             crud_secretary_maas_rating)
from app.services.errors.exceptions import NotFoundError


class CRUDSecretary(CRUDBase):

    def create_secretary(self, schema):
        dict_body = request.get_json()

        item = self.class_model().create_item(dict_body).save()

        if 'address' in dict_body:
            dict_body['address']['secretary_id'] = item.id
            crud_secretary_address.post(dict_body=dict_body['address'])

        if 'maas_rating' in dict_body:
            for maas_dict in dict_body['maas_rating']:
                maas_dict['secretary_id'] = item.id
                crud_secretary_maas_rating.post(dict_body=maas_dict)

        if schema:
            item = self.class_schema().dump(item)

        return item

    def update_secretary_address(self, item_id):
        dict_body = request.get_json()['address']
        address = models.SecretaryAddress.query.filter_by(id=item_id).first()
        if "city_id" in dict_body:
            city = models.City.query.filter(
                models.City.id == dict_body["city_id"]).first()
            if city is None:
                raise NotFoundError("Cidade não encontrada")

        item = address.update(**dict_body)
        item = self.class_schema().dump(item)
        return item

    def update_secretary(self, item_id):
        dict_body = request.get_json()

        item = self.put(item_id, dict_body=dict_body)

        if 'address' in dict_body:
            self.update_secretary_address(item.address.id)

        if 'maas_rating' in dict_body:
            for maas_dict in dict_body['maas_rating']:
                maas_dict['secretary_id'] = item.id
                crud_secretary_maas_rating.post(dict_body=maas_dict)
        item = self.get(item_id)
        item = self.class_schema().dump(item)

        return item


crud_secretary = CRUDSecretary(models.Secretary,
                               schemas.SecretarySchema)
