from flask import request, Blueprint
from flask_jwt_extended import jwt_required

from app.controllers import crud_group, crud_main_company, \
    crud_main_settings

from app.services.requests.intercept import intercept_admin_user
from app.services.requests.requests import default_return

main_bp = Blueprint("main", __name__, url_prefix='/main')


@main_bp.route('', methods=['GET', 'PUT'])
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
              schema: MainCompanySchema
      tags:
          - Main Company

    put:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: MainCompanySchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: MainCompanySchema
      tags:
          - Main Company
    """
    try:
        if request.method == 'GET':
            item = crud_main_company.get_first(schema=True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_group.put_first(True)
            return default_return(200, 3, item)

    except Exception as e:
        raise e


@main_bp.route('/settings', methods=['GET', 'PUT'])
@jwt_required()
@intercept_admin_user
def item_configuration_routes():
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
              schema: MainConfigurationSchema
      tags:
          - Main Company

    put:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: MainConfigurationSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: MainCompanySchema
      tags:
          - Main Company
    """
    try:
        if request.method == 'GET':
            item = crud_main_settings.get_first(schema=True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_main_settings.put_first(True)
            return default_return(200, 3, item)

    except Exception as e:
        raise e
