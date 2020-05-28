from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

# la carpeta app es un modulo 
app = Flask(__name__)

mail = Mail()
db = SQLAlchemy()
csrf = CSRFProtect()
bootstrap = Bootstrap()# es la encarga de el diseno
login_manager = LoginManager()

from .views import page
from .models import User, Task
from .consts import LOGIN_REQUIRED

def create_app(config):
    app.config.from_object(config)
    
    csrf.init_app(app)# validad la autencicidad de las peticiones 
    if not app.config.get('TEST',False):
        bootstrap.init_app(app)

    app.app_context().push()

    login_manager.init_app(app)
    login_manager.login_view = '.login' # url whent try acces to other url
    login_manager.login_message = 'es necesario iniciar sesion'
    
    mail.init_app(app)

    app.register_blueprint(page)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app

