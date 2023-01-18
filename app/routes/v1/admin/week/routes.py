from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError

from app.controllers import crud_week
from app.services.errors.exceptions import GenerateError
from app.services.requests.intercept import intercept_admin_user
from app.services.requests.requests import default_return

week_bp = Blueprint("week_bp", __name__, url_prefix="/weeks")


@week_bp.route('', methods=['GET', 'POST'])
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
              schema: WeekSchema
      tags:
          - Week

    post:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: WeekSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: WeekSchema
      tags:
          - Week
    """
    try:
        if request.method == 'GET':
            school_class_id = request.args.get('class_id')
            category_id = request.args.get('category_id')
            extra_filters = None
            if school_class_id:
              extra_filters.append([('category_id', 'eq', category_id)])
              extra_filters.append([('school_class_id', 'eq', school_class_id)])
            items, items_paginate = crud_week.get_multi(True, extra_filters=extra_filters)
            return default_return(200, 2, items, items_paginate)

        if request.method == 'POST':
            item = crud_week.post(schema=True)
            return default_return(201, 1, item)
    except IntegrityError:
        raise GenerateError("One of the foreign keys was not found", 400)
    except Exception as e:
        raise e


@week_bp.route('/<item_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
@intercept_admin_user
def item_routes(item_id):
    """
    ---
    get:
      security:
        - jwt: []
      description: Week
      parameters:
        - path_params_default
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: WeekSchema
      tags:
          - Week

    put:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: WeekSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: WeekSchema
      tags:
          - Week

    delete:
      security:
        - jwt: []
      description: Week
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: WeekSchema
      tags:
          - Week
    """
    try:
        if request.method == 'GET':
            item = crud_week.get(item_id, True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_week.put(item_id, True)
            return default_return(200, 3, item)

        if request.method == 'DELETE':
            crud_week.delete(item_id)
            return default_return(204, 4)
    except Exception as e:
        raise e
