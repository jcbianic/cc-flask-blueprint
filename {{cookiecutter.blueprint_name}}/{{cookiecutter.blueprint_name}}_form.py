from flask_wtf import FlaskForm as Form
from wtforms import TextField
from wtforms.validators import Required


class {{cookiecutter.blueprint_name.capitalize()}}CreateForm(Form):
    name = TextField("name", validators=[Required(message="Name required")])


class {{cookiecutter.blueprint_name.capitalize()}}UpdateForm(Form):
    name = TextField("name", validators=[Required(message="Name required")])
