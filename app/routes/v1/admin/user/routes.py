from flask import request, Blueprint
from flask_jwt_extended import jwt_required

from app.controllers.user import crud_user
from app.services.requests.intercept import intercept_admin_user
from app.services.requests.requests import default_return

user_bp = Blueprint("user_bp", __name__, url_prefix="/users")


@user_bp.route('', methods=['GET', 'POST'])
@jwt_required()
@intercept_admin_user
def item_multi_routes():
    """
    ---
    get:
      security:
        - jwt: []
      parameters:
        - page_param
        - per_page_param
        - search_param
        - in: query
          name: group_id
          description: Users' group id
          schema:
            type: integer
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: UserSchema
      tags:
          - User

    post:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: UserSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: UserSchema
      tags:
          - User
    """
    try:
        if request.method == 'GET':
            items, items_paginate = crud_user.list_users()
            return default_return(200, 2, items, items_paginate)

        if request.method == 'POST':
            item = crud_user.create_user_with_exist(schema=True,
                                                    exist_taxpayer=True)
            return default_return(201, 1, item)

    except Exception as e:
        raise e


@user_bp.route('/<item_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
@intercept_admin_user
def item_routes(item_id):
    """
    ---
    get:
      security:
        - jwt: []
      description: User
      parameters:
        - path_params_default
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: UserSchema
      tags:
          - User

    put:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: UserSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: UserSchema
      tags:
          - User

    delete:
      security:
        - jwt: []
      description: User
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: UserSchema
      tags:
          - User
    """
    try:
        if request.method == 'GET':
            item = crud_user.get(item_id, True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_user.update_user(item_id)
            return default_return(200, 3, item)

        if request.method == 'DELETE':
            crud_user.delete(item_id)
            return default_return(204, 4)
    except Exception as e:
        raise e
