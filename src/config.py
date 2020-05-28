from decouple import config 

class Config: 
    SECRET_KEY = 'codigofacilito' 
    

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:MyNewPass@localhost/project_web_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'#'smtp.googlemail.com'#
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'infointotech5@gmail.com'
    MAIL_PASSWORD =  'Ytrewq123456'#config('MAIL_PASSWORD')#MAIL_PASSWORD #lib = OS   #lib decouple  este la blave como variable de entorno 


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:MyNewPass@localhost/project_web_flask_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEST = True 
config ={
    'development':DevelopmentConfig,
    'default': DevelopmentConfig,
    'test': TestConfig
}