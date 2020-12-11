from app import db
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask-login import login_required

from .{{cookiecutter.blueprint_name}}_model import {{cookiecutter.blueprint_name.capitalize()}}
from .{{cookiecutter.blueprint_name}}_form import {{cookiecutter.blueprint_name.capitalize()}}CreateForm, {{cookiecutter.blueprint_name.capitalize()}}UpdateForm


from app.common.helpers import set_logger

{{cookiecutter.blueprint_name}} = Blueprint("{{cookiecutter.blueprint_name}}", __name__, template_folder="templates")
log = set_logger(__name__)


@{{cookiecutter.blueprint_name}}.route("/")
@{{cookiecutter.blueprint_name}}.route("/index")
@login_required
def index():
    {{cookiecutter.blueprint_name}}s = {{cookiecutter.blueprint_name.capitalize()}}.query.all()
    return render_template('{{cookiecutter.blueprint_name}}-index.html', {{cookiecutter.blueprint_name}}s={{cookiecutter.blueprint_name}}s)


@{{cookiecutter.blueprint_name}}.route("/<int:id>")
@login_required
def view(id):
    {{cookiecutter.blueprint_name}} = {{cookiecutter.blueprint_name.capitalize()}}.query.get(id)
    return render_template('{{cookiecutter.blueprint_name}}-view.html', {{cookiecutter.blueprint_name}}={{cookiecutter.blueprint_name}})


@{{cookiecutter.blueprint_name}}.route("/create")
@login_required
def create():
    form = {{cookiecutter.blueprint_name.capitalize()}}CreateForm()
    if request.method == "GET":
        return render_template('{{cookiecutter.blueprint_name}}-create.html', form=form)
    if request.method == "POST":
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
    

@{{cookiecutter.blueprint_name}}.route("/update/<int:id>", methods=["GET", "POST"])
@login_required
def update(id):
    {{cookiecutter.blueprint_name}} = {{cookiecutter.blueprint_name.capitalize()}}.query.get(id)
    form = {{cookiecutter.blueprint_name.capitalize()}}UpdateForm()
    if request.method == "GET":
        
        return render_template('{{cookiecutter.blueprint_name}}-update.html', form=form)
    if request.method == "POST":
        if form.validate_on_submit():
            {{cookiecutter.blueprint_name}}.update(form.data)
            db.session.add({{cookiecutter.blueprint_name}})
            db.session.commit()
            flash("was updated", "is-success")
    return render_template('{{cookiecutter.blueprint_name}}-view.html', {{cookiecutter.blueprint_name}}={{cookiecutter.blueprint_name}})


@{{cookiecutter.blueprint_name}}.route("/delete/<int:id>", methods=["GET"])
@login_required
def delete(id):
    {{cookiecutter.blueprint_name}} = {{cookiecutter.blueprint_name.capitalize()}}.query.get(id)
    if {{cookiecutter.blueprint_name}}:
        db.session.delete({{cookiecutter.blueprint_name}})
        db.session.commit()
        flash(
            "{{cookiecutter.blueprint_name.capitalize()}} {} was successfully deleted.".format({{cookiecutter.blueprint_name}}.name), "is-warning"
        )
    else:
        flash("Incorrect ID: {{cookiecutter.blueprint_name.capitalize()}} with id {} was not found.".format(id), "is-error")
    return redirect(url_for("{{cookiecutter.blueprint_name}}.index"))


@{{cookiecutter.blueprint_name}}.route("/delete", methods=["GET"])
@login_required
def delete_all():
    delete_count = {{cookiecutter.blueprint_name.capitalize()}}.query.delete()
    db.session.commit()
    flash("All {:} {{cookiecutter.blueprint_name}} were deleted.".format(delete_count), "is-warning")
    return redirect(url_for("{{cookiecutter.blueprint_name}}.index"))

