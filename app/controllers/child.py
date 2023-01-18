
from flask import request

from app import models, schemas
from app.controllers import CRUDBase
from app.services.child.relationship import (clear_child_parents,
                                             create_child_parents)


class CRUDChild(CRUDBase):

    def create_child(self):
        dict_body = request.get_json()

        item = self.class_model().create_item(dict_body).save()

        create_child_parents(item, dict_body)
        
        item = self.class_schema().dump(item)

        return item

    def update_child(self, item_id):
        dict_body = request.get_json()

        item = self.put(item_id, dict_body=dict_body)
        clear_child_parents(item.id)
        create_child_parents(item, dict_body)
        item = self.get(item_id)
        item = self.class_schema().dump(item)

        return item


crud_child = CRUDChild(models.Child, schemas.ChildSchema)
