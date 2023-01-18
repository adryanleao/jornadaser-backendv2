from .routes import client_bp


def init_app(v1_bp):
    v1_bp.register_blueprint(client_bp)
