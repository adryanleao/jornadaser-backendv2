from flask import Blueprint

from app.controllers import crud_main_settings
from app.services.requests.requests import default_return

settings_bp = Blueprint('settings', __name__, url_prefix="/settings")


@settings_bp.route('', methods=['GET', 'POST'])
def item_multi_routes():
    """
    ---
    get:
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: MainSettings
      tags:
          - Main Settings

    post:
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
          - Main Settings
    """
    try:
        item = crud_main_settings.get_first(schema=True)
        return default_return(200, 2, item)

    except Exception as e:
        raise e
