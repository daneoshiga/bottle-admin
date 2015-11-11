# -*- coding: utf-8 -*-
from bottle_admin import Admin
from bottle import Bottle

from .controllers.home import home_app
from .controllers.user import user_app


Routes = Bottle()
admin = Admin(app=Routes)
# App to render / (home)
Routes.merge(home_app)
# Mount other applications
Routes.mount("/user", user_app)
