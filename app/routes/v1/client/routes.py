from flask import request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.controllers.user import crud_user
from app.services.jwt.token import generate_user_jwt
from app.services.requests.requests import default_return

client_bp = Blueprint('client', __name__, url_prefix="/client")


@client_bp.route('', methods=['POST'])
def item_multi_routes():
    """
    ---
    post:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: User
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: User
      tags:
          - Client
    """
    try:
        item = crud_user.create_user_with_exist(schema=True,
                                                specific_group_id=5)
        item['auth'] = generate_user_jwt(item)
        return default_return(201, 1, item)
    except Exception as e:
        raise e


@client_bp.route('', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def item_routes():
    """
    ---
    get:
      security:
        - jwt: []
      description: State
      parameters:
        - path_params_default
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: User
      tags:
          - Client

    put:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: User
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: User
      tags:
          - Client

    delete:
      security:
        - jwt: []
      description: State
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: State
      tags:
          - Client
    """
    try:
        user_jwt = get_jwt_identity()
        if request.method == 'GET':
            item = crud_user.get_user_by_jwt(user_jwt, True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_user.put(user_jwt['user_id'], True)
            return default_return(200, 3, item)

        if request.method == 'DELETE':
            crud_user.delete(user_jwt['user_id'])
            return default_return(204, 4)
    except Exception as e:
        raise e


@client_bp.route('/address', methods=['GET'])
@jwt_required()
def cep_route():
    """
    ---
    get:
      security:
        - jwt: []
      description: State
      parameters:
        - path_params_default
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: User
      tags:
          - Client
    """
    try:
        if request.method == 'GET':
            item = crud_user.find_cep()
            return default_return(200, 2, item)
    except Exception as e:
        raise e
