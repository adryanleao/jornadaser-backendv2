from .routes import class_bp


def init_app(app):
    """
    It registers the user_bp blueprint to the app
    
    :param app: The Flask application instance
    """
    app.register_blueprint(class_bp)
