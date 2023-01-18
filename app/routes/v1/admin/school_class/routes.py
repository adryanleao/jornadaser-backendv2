from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.controllers import crud_school_class
from app.services.requests.intercept import intercept_admin_user
from app.services.requests.requests import default_return

class_bp = Blueprint("class_bp", __name__, url_prefix="/classes")


@class_bp.route('', methods=['GET', 'POST'])
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
              schema: SchoolClassSchema
      tags:
          - SchoolClass

    post:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: SchoolClassSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: SchoolClassSchema
      tags:
          - SchoolClass
    """
    try:
        if request.method == 'GET':
            items, items_paginate = crud_school_class.get_multi(True)
            return default_return(200, 2, items, items_paginate)

        if request.method == 'POST':
            item = crud_school_class.post(schema=True)
            return default_return(201, 1, item)

    except Exception as e:
        raise e


@class_bp.route('/<item_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
@intercept_admin_user
def item_routes(item_id):
    """
    ---
    get:
      security:
        - jwt: []
      description: SchoolClass
      parameters:
        - path_params_default
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: SchoolClassSchema
      tags:
          - SchoolClass

    put:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: SchoolClassSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: SchoolClassSchema
      tags:
          - SchoolClass

    delete:
      security:
        - jwt: []
      description: SchoolClass
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: SchoolClassSchema
      tags:
          - SchoolClass
    """
    try:
        if request.method == 'GET':
            item = crud_school_class.get(item_id, True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_school_class.put(item_id, True)
            return default_return(200, 3, item)

        if request.method == 'DELETE':
            crud_school_class.delete(item_id)
            return default_return(204, 4)
    except Exception as e:
        raise e
