from app.routes.v1.admin import (category, child, city, community, content,
                                 country, extra_material, group, institution,
                                 maas, main, notification, school_class,
                                 secretary, state, team, user, week)
from app.routes.v1.admin.routes import admin_bp


def init_app(v1_bp):
    """
    It registers the admin_bp blueprint to the v1_bp blueprint
    
    :param v1_bp: The blueprint for the version 1 of the API
    """
    main.init_app(admin_bp)
    category.init_app(admin_bp)
    city.init_app(admin_bp)
    child.init_app(admin_bp)
    country.init_app(admin_bp)
    content.init_app(admin_bp)
    state.init_app(admin_bp)
    community.init_app(admin_bp)
    group.init_app(admin_bp)
    user.init_app(admin_bp)
    secretary.init_app(admin_bp)
    school_class.init_app(admin_bp)
    institution.init_app(admin_bp)
    extra_material.init_app(admin_bp)
    notification.init_app(admin_bp)
    maas.init_app(admin_bp)
    team.init_app(admin_bp)
    week.init_app(admin_bp)
    v1_bp.register_blueprint(admin_bp)
