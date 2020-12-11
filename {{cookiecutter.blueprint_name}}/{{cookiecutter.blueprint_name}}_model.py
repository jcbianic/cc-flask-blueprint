from app import db

class {{cookiecutter.blueprint_name.capitalize()}}(db.Model):
    id = db.Column(db.Integer, primary_key=True)
