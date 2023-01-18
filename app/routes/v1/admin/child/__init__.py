from .routes import child_bp


def init_app(app):
    """
    It registers the child_bp blueprint to the app
    
    :param app: The Flask application instance
    """
    app.register_blueprint(child_bp)
