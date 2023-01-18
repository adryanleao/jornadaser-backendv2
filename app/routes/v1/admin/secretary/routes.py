from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.controllers.secretary import crud_secretary
from app.services.requests.intercept import intercept_admin_user
from app.services.requests.requests import default_return

secretary_bp = Blueprint("secretary_bp", __name__, url_prefix="/secretaries")


@secretary_bp.route('', methods=['GET', 'POST'])
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
              schema: SecretarySchema
      tags:
          - Secretary

    post:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: SecretarySchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: SecretarySchema
      tags:
          - Secretary
    """
    try:
        if request.method == 'GET':
            items, items_paginate = crud_secretary.get_multi(True)
            return default_return(200, 2, items, items_paginate)

        if request.method == 'POST':
            item = crud_secretary.create_secretary(schema=True)
            return default_return(201, 1, item)

    except Exception as e:
        raise e


@secretary_bp.route('/<item_id>', methods=['GET', 'PUT', 'DELETE'])
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
              schema: SecretarySchema
      tags:
          - Secretary

    put:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: SecretarySchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: SecretarySchema
      tags:
          - Secretary

    delete:
      security:
        - jwt: []
      description: Secretary
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: SecretarySchema
      tags:
          - Secretary
    """
    try:
        if request.method == 'GET':
            item = crud_secretary.get(item_id, True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_secretary.update_secretary(item_id)
            return default_return(200, 3, item)

        if request.method == 'DELETE':
            crud_secretary.delete(item_id)
            return default_return(204, 4)
    except Exception as e:
        raise e
