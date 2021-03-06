# users-service/project/__init__.py

import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

# instantiate the db
db = SQLAlchemy()
# instantiate flask migrate
migrate = Migrate()
bcrypt = Bcrypt()


def create_app():

    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    # /users
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)
    # /auth
    from project.api.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
