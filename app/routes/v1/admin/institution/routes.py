from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.controllers.institution import crud_institution
from app.services.requests.intercept import intercept_admin_user
from app.services.requests.requests import default_return

institution_bp = Blueprint("institution_bp", __name__, url_prefix="/institutions")


@institution_bp.route('', methods=['GET', 'POST'])
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
              schema: InstitutionSchema
      tags:
          - Institution

    post:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: InstitutionSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: InstitutionSchema
      tags:
          - Institution
    """
    try:
        if request.method == 'GET':
            items, items_paginate = crud_institution.get_multi(True)
            return default_return(200, 2, items, items_paginate)

        if request.method == 'POST':
            item = crud_institution.create_institution(schema=True)
            return default_return(201, 1, item)

    except Exception as e:
        raise e


@institution_bp.route('/<item_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
@intercept_admin_user
def item_routes(item_id):
    """
    ---
    get:
      security:
        - jwt: []
      description: Institution
      parameters:
        - path_params_default
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: InstitutionSchema
      tags:
          - Institution

    put:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: InstitutionSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: InstitutionSchema
      tags:
          - Institution

    delete:
      security:
        - jwt: []
      description: Institution
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: InstitutionSchema
      tags:
          - Institution
    """
    try:
        if request.method == 'GET':
            item = crud_institution.get(item_id, True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_institution.update_institution(item_id)
            return default_return(200, 3, item)

        if request.method == 'DELETE':
            crud_institution.delete(item_id)
            return default_return(204, 4)
    except Exception as e:
        raise e
