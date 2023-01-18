from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.controllers import crud_maas
from app.services.requests.intercept import intercept_admin_user
from app.services.requests.requests import default_return

maas_bp = Blueprint("maas_bp", __name__, url_prefix="/maas")


@maas_bp.route('', methods=['GET', 'POST'])
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
            items, items_paginate = crud_maas.get_multi(True)
            return default_return(200, 2, items, items_paginate)

        if request.method == 'POST':
            item = crud_maas.post(schema=True)
            return default_return(201, 1, item)

    except Exception as e:
        raise e


@maas_bp.route('/<item_id>', methods=['GET', 'PUT', 'DELETE'])
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
            item = crud_maas.get(item_id, True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_maas.put(item_id, True)
            return default_return(200, 3, item)

        if request.method == 'DELETE':
            crud_maas.delete(item_id)
            return default_return(204, 4)
    except Exception as e:
        raise e
