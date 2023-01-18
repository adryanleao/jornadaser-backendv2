from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError

from app.controllers import crud_extra_material
from app.services.errors.exceptions import GenerateError
from app.services.requests.intercept import intercept_admin_user
from app.services.requests.requests import default_return

extra_material_bp = Blueprint("extra_material_bp", __name__, url_prefix="/extra_materials")


@extra_material_bp.route('', methods=['GET', 'POST'])
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
              schema: ExtraMaterialSchema
      tags:
          - ExtraMaterial

    post:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: ExtraMaterialSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: ExtraMaterialSchema
      tags:
          - ExtraMaterial
    """
    try:
        if request.method == 'GET':
            items, items_paginate = crud_extra_material.get_multi(True)
            return default_return(200, 2, items, items_paginate)

        if request.method == 'POST':
            item = crud_extra_material.post(schema=True)
            return default_return(201, 1, item)
    except IntegrityError:
        raise GenerateError("One of the foreign keys was not found", 400)
    except Exception as e:
        raise e


@extra_material_bp.route('/<item_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
@intercept_admin_user
def item_routes(item_id):
    """
    ---
    get:
      security:
        - jwt: []
      description: Secretary
      parameters:
        - path_params_default
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: ExtraMaterialSchema
      tags:
          - ExtraMaterial

    put:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: ExtraMaterialSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: ExtraMaterialSchema
      tags:
          - ExtraMaterial

    delete:
      security:
        - jwt: []
      description: ExtraMaterialSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: ExtraMaterialSchema
      tags:
          - ExtraMaterial
    """
    try:
        if request.method == 'GET':
            item = crud_extra_material.get(item_id, True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_extra_material.put(item_id, True)
            return default_return(200, 3, item)

        if request.method == 'DELETE':
            crud_extra_material.delete(item_id)
            return default_return(204, 4)
    except Exception as e:
        raise e
