from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.controllers.team import crud_team
from app.services.requests.intercept import intercept_admin_user
from app.services.requests.requests import default_return

team_bp = Blueprint("team_bp", __name__, url_prefix="/teams")


@team_bp.route('', methods=['GET', 'POST'])
@jwt_required()
@intercept_admin_user
def item_multi_routes():
    """
    ---
    get:
      security:
        - jwt: []
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: MaasSchema
      tags:
          - Maas

    post:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: MaasSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: MaasSchema
      tags:
          - Maas
    """
    try:
        if request.method == 'GET':
            institution_id = request.args.get('institution_id')
            extra_filters = None
            if institution_id:
              extra_filters = [('institution_id', 'eq', institution_id)]
            items, items_paginate = crud_team.get_multi(True, extra_filters=extra_filters)
            return default_return(200, 2, items, items_paginate)

        if request.method == 'POST':
            item = crud_team.create_team()
            return default_return(201, 1, item)

    except Exception as e:
        raise e


@team_bp.route('/<item_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
@intercept_admin_user
def item_routes(item_id):
    """
    ---
    get:
      security:
        - jwt: []
      description: Maas
      parameters:
        - path_params_default
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: MaasSchema
      tags:
          - Maas

    put:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: MaasSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: MaasSchema
      tags:
          - Maas

    delete:
      security:
        - jwt: []
      description: Maas
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: MaasSchema
      tags:
          - Maas
    """
    try:
        if request.method == 'GET':
            item = crud_team.get(item_id, True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_team.put(item_id, True)
            return default_return(200, 3, item)

        if request.method == 'DELETE':
            crud_team.delete(item_id)
            return default_return(204, 4)
    except Exception as e:
        raise e
