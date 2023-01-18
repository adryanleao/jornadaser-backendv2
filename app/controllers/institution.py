
from app.services.errors.exceptions import NotFoundError
from flask import request

from app import models, schemas
from app.controllers import CRUDBase, crud_institution_address


class CRUDInstitution(CRUDBase):

    def create_institution(self, schema):
        dict_body = request.get_json()

        item = self.class_model().create_item(dict_body).save()

        if 'address' in dict_body:
            dict_body['address']['institution_id'] = item.id
            crud_institution_address.post(dict_body=dict_body['address'])

        if schema:
            item = self.class_schema().dump(item)

        return item

    def update_institution_address(self, item_id):
        dict_body = request.get_json()['address']
        address = models.InstitutionAddress.query.filter_by(id=item_id).first()
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

    def update_institution(self, item_id):
        dict_body = request.get_json()

        item = self.put(item_id, dict_body=dict_body)

        if 'address' in dict_body:
            self.update_institution_address(item.address.id)

        item = self.get(item_id)
        item = self.class_schema().dump(item)

        return item


crud_institution = CRUDInstitution(models.Institution,
                                   schemas.InstitutionSchema)
