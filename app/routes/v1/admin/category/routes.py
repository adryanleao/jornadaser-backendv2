from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.controllers import crud_category
from app.services.requests.intercept import intercept_admin_user
from app.services.requests.requests import default_return

category_bp = Blueprint("category_bp", __name__, url_prefix="/categories")


@category_bp.route('', methods=['GET', 'POST'])
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
              schema: CategorySchema
      tags:
          - Category

    post:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: CategorySchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: CategorySchema
      tags:
          - Category
    """
    try:
        if request.method == 'GET':
            items, items_paginate = crud_category.get_multi(True)
            return default_return(200, 2, items, items_paginate)

        if request.method == 'POST':
            item = crud_category.post(schema=True)
            return default_return(201, 1, item)

    except Exception as e:
        raise e


@category_bp.route('/<item_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
@intercept_admin_user
def item_routes(item_id):
    """
    ---
    get:
      security:
        - jwt: []
      description: Category
      parameters:
        - path_params_default
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: CategorySchema
      tags:
          - Category

    put:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: CategorySchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: CategorySchema
      tags:
          - Category

    delete:
      security:
        - jwt: []
      description: Category
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: CategorySchema
      tags:
          - Category
    """
    try:
        if request.method == 'GET':
            item = crud_category.get(item_id, True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_category.put(item_id, True)
            return default_return(200, 3, item)

        if request.method == 'DELETE':
            crud_category.delete(item_id)
            return default_return(204, 4)
    except Exception as e:
        raise e


@category_bp.route('/<int:item_id>/images', methods=['PUT', 'DELETE'])
@jwt_required()
@intercept_admin_user
def item_image(item_id):
    """
    ---
    put:
      security:
      - jwt: []
      parameters:
      - path_params_default
      requestBody:
        required: true
        content:
          application/json:
            schema: FileUpdate
            example:
              file: data:image/png;base64,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
      responses:
        '200':
          description: Updated successfully
          content:
            application/json:
              schema: ImageReturnSchema
      tags:
          - Admin Army Rank

    delete:
      security:
      - jwt: []
      parameters:
      - path_params_default
      responses:
        '200':
          description: Deleted successfully
      tags:
          - Admin Army Rank
    """
    try:

        if request.method == 'PUT':
            item = crud_category.put_image(item_id=item_id, path="categories")
            return default_return(200, 3, item)

        if request.method == 'DELETE':
            crud_category.delete_image(item_id)
            return default_return(200, 4)
    except Exception as e:
        raise e
