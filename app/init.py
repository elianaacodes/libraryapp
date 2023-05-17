from flask import Flask 
from config import Config 
from .site.routes import site 
from .authentication.routes import auth 

from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from models import db as root_db, login_manager, ma 

app = Flask (__name__) 

app.register_blueprint(site)
app.config.from_object(Config)
root_db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate (app, root_db)


