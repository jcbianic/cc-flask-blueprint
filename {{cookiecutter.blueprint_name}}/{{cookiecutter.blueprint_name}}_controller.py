from flask import Blueprint

from app.common.helpers import set_logger

{{cookiecutter.blueprint_name}} = Blueprint("{{cookiecutter.blueprint_name}}", __name__, template_folder="templates")
log = set_logger(__name__)

@{{cookiecutter.blueprint_name}}.route("/")
@{{cookiecutter.blueprint_name}}.route("/index")
def index():
    return render_template('{{cookiecutter.blueprint_name}}-index.html')

@{{cookiecutter.blueprint_name}}.route("/<int:id>")
def view(id):
    {{cookiecutter.blueprint_name}} = {{cookiecutter.blueprint_name.capitalize()}}.query.get(id)
    return render_template('{{cookiecutter.blueprint_name}}-view.html', {{cookiecutter.blueprint_name}}={{cookiecutter.blueprint_name}})

@{{cookiecutter.blueprint_name}}.route("/create")
def create():
    form = Create{{cookiecutter.blueprint_name.capitalize()}}()
    if method == "GET":
        return render_template('{{cookiecutter.blueprint_name}}-create.html', form=form)
    if method == "POST":
        if form.validate_on_submit():
            new_{{cookiecutter.blueprint_name}} = {{cookiecutter.blueprint_name.capitalize()}}(form.data)
            db.session.add(new_{{cookiecutter.blueprint_name}})
            db.session.commit()
            flash("New {{cookiecutter.blueprint_name}} was created", "is-success")
            return redirect(url_for("{{cookiecutter.blueprint_name}}.view", id=new_{{cookiecutter.blueprint_name}}.id))
        else:
            flash("Creation of {{cookiecutter.blueprint_name}} failed.", "is-warning")
            log.warning("Creation of {{cookiecutter.blueprint_name}} failed.")
            for e in form.errors:
                log.warning(e)
            return redirect(url_for("{{cookiecutter.blueprint_name}}.create"))
    

@{{cookiecutter.blueprint_name}}.route("/update/<int:id>", methods=["GET", "PUT"])
def update(id):
    {{cookiecutter.blueprint_name}} = {{cookiecutter.blueprint_name.capitalize()}}.query.get(id)
    return render_template('{{cookiecutter.blueprint_name}}-view.html', {{cookiecutter.blueprint_name}}={{cookiecutter.blueprint_name}})