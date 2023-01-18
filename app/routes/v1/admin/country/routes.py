from flask import request, Blueprint
from flask_jwt_extended import jwt_required

from app.controllers import crud_country
from app.services.requests.intercept import intercept_admin_user
from app.services.requests.requests import default_return

country_bp = Blueprint('country', __name__, url_prefix="/countries")


@country_bp.route('', methods=['GET', 'POST'])
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
              schema: CountrySchema
      tags:
          - Country

    post:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: CountrySchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: CountrySchema
      tags:
          - Country
    """
    try:
        if request.method == 'GET':
            items, items_paginate = crud_country.get_multi(True)
            return default_return(200, 2, items, items_paginate)

        if request.method == 'POST':
            item = crud_country.post(schema=True)
            return default_return(201, 1, item)

    except Exception as e:
        raise e


@country_bp.route('/<item_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
@intercept_admin_user
def item_routes(item_id):
    """
    ---
    get:
      security:
        - jwt: []
      description: City
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: CountrySchema
      tags:
          - Country

    put:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: CountrySchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: CountrySchema
      tags:
          - Country

    delete:
      security:
        - jwt: []
      description: City
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: CountrySchema
      tags:
          - Country
    """
    try:
        if request.method == 'GET':
            item = crud_country.get(item_id, True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_country.put(item_id, True)
            return default_return(200, 3, item)

        if request.method == 'DELETE':
            crud_country.delete(item_id)
            return default_return(204, 4)
    except Exception as e:
        raise e
