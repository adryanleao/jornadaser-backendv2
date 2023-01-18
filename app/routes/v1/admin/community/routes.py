from flask import request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.controllers import crud_community
from app.services.requests.intercept import intercept_admin_user
from app.services.requests.requests import default_return

community_bp = Blueprint('community', __name__, url_prefix="/communities")


@community_bp.route('', methods=['GET', 'POST'])
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
              schema: CommunitySchema
      tags:
          - Community

    post:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: CommunitySchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: CommunitySchema
      tags:
          - Community
    """
    try:
        user_jwt = get_jwt_identity()
        if request.method == 'GET':
            extra_filters = [("user_id", "eq", user_jwt['user_id'])]
            items, items_paginate = crud_community.get_multi(True, extra_filters=extra_filters)
            return default_return(200, 2, items, items_paginate)

        if request.method == 'POST':
            extra_fields = [("user_id", user_jwt['user_id'])]
            item = crud_community.post(schema=True, extra_fields=extra_fields)
            return default_return(201, 1, item)

    except Exception as e:
        raise e


@community_bp.route('/<item_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
@intercept_admin_user
def item_routes(item_id):
    """
    ---
    get:
      security:
        - jwt: []
      description: Community
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: CommunitySchema
      tags:
          - Community

    put:
      security:
        - jwt: []
      requestBody:
        description: Optional description in *Markdown*
        required: true
        content:
          application/json:
            schema: CommunitySchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: CommunitySchema
      tags:
          - Community

    delete:
      security:
        - jwt: []
      description: Community
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: CommunitySchema
      tags:
          - Community
    """
    try:
        if request.method == 'GET':
            item = crud_community.get(item_id, True)
            return default_return(200, 2, item)

        if request.method == 'PUT':
            item = crud_community.put(item_id, True)
            return default_return(200, 3, item)

        if request.method == 'DELETE':
            crud_community.delete(item_id)
            return default_return(204, 4)
    except Exception as e:
        raise e