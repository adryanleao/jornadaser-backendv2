
from flask import request

from app import models, schemas
from app.controllers import CRUDBase
from app.services.team.relationship import create_team_students


class CRUDTeam(CRUDBase):

    def create_team(self):
        
        dict_body = request.get_json()

        item = self.post(dict_body=dict_body)
            
        create_team_students(item, dict_body)
        item = self.class_schema().dump(item)

        return item

    def update_user(self, item_id):
        dict_body = request.get_json()

        item = self.put(item_id, dict_body=dict_body)

        create_team_students(item, dict_body)
        item = self.get(item_id)
        item = self.class_schema().dump(item)

        return item


crud_team = CRUDTeam(models.Team, schemas.TeamSchema)
