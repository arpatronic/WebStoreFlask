from wtforms import Form
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField, HiddenField,TextAreaField
from wtforms.fields.html5 import EmailField

from .models import User

def codi_vadilator(form, field):
    if field.data  == 'codi' or field.data == 'Codi':
        raise validators.ValidationError('el username  codi no es permitido')
    
def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('Solo los humanos pueden completar el registro')


class LoginForm(Form):
    username = StringField('Username',[
        validators.length(min=4,max = 50, message='El el nombre de usuario debe tener 4-50 caracteres' )
    ])
    password = PasswordField('Password',[
        validators.Required()
    ])

class RegisterForm(Form):
    username = StringField('Username',[
        validators.length(min=4 , max=50),
        codi_vadilator
    ])
    honeypot = HiddenField("",[length_honeypot])
    email =  EmailField('Correo electronico',[
        validators.length(min=6, max =100),
        validators.Required(message= 'El email es requerido.'),
        validators.Email(message='ingrese un email Valido.')
    ])
    password = PasswordField('Password',[
        validators.Required('El password es requerido'),
        validators.EqualTo('confirm_password', message =  'La contraseña no coincide')
    ])
    confirm_password = PasswordField('Confirm password')
    accept = BooleanField('',[
        validators.DataRequired()
    ])
    
    def validate_username(self,username	):
        if User.get_by_username(username.data):
            raise validators.ValidationError(' El username ya se encuentra en uso ')

    def validate_email(self,email):
        if User.get_by_email(email.data):
            raise validators.ValidationError(' El email ya se encuentra en uso ')

    # se esta sobrescribiendo el  metodo 
    def validate(self):
        if not Form.validate(self):
            return False
        if len(self.password.data) < 3:
            self.password.errors.append('el password es demaciado corto')
            return False
        return True

class TaskForm(Form):
    title = StringField('Titulo',[
        validators.length(min=4, max = 50, message='Titulo fura de rango'),
        validators.DataRequired(message = 'El titulo es requerido')
    ])
    description = TextAreaField('Descripcion', [
        validators.DataRequired(message = 'La descripcion es requerida ')
    ], render_kw = {'rows':5} )