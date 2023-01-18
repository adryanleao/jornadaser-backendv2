from flask import request, Blueprint
from flask_jwt_extended import jwt_required

from app.controllers.child import crud_child
from app.services.requests.intercept import intercept_admin_user
from app.services.requests.requests import default_return

child_bp = Blueprint("child_bp", __name__, url_prefix="/children")


@child_bp.route('', methods=['GET', 'POST'])
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
              schema: ChildSchema
      tags:
          - Child

    post:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: ChildSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: ChildSchema
      tags:
          - Child
    """
    try:
        if request.method == 'GET':
            items, items_paginate = crud_child.get_multi(True)
            return default_return(200, 2, items, items_paginate)

        if request.method == 'POST':
            item = crud_child.create_child()
            return default_return(201, 1, item)

    except Exception as e:
        raise e


@child_bp.route('/<item_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
@intercept_admin_user
def item_routes(item_id):
    """
    ---
    get:
      security:
        - jwt: []
      description: Child
      parameters:
        - path_params_default
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: ChildSchema
      tags:
          - Child

    put:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: ChildSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: ChildSchema
      tags:
          - Child

    delete:
      security:
        - jwt: []
      description: Child
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: ChildSchema
      tags:
          - Child
    """
    try:
        if request.method == 'GET':
            item = crud_child.get(item_id, True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_child.update_child(item_id)
            return default_return(200, 3, item)

        if request.method == 'DELETE':
            crud_child.delete(item_id)
            return default_return(204, 4)
    except Exception as e:
        raise e
