from .routes import week_bp


def init_app(app):
    """
    It registers the user_bp blueprint to the app
    
    :param app: The Flask application instance
    """
    app.register_blueprint(week_bp)
