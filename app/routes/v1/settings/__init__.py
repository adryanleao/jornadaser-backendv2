from .routes import settings_bp


def init_app(v1_bp):
    v1_bp.register_blueprint(settings_bp)
