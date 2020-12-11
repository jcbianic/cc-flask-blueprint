# cc-flask-blueprint

Cookiecutter template for new flask blueprint.

## Dependencies

* flask (obviously)
* flask-login
* flask-wtf

For templates :
* CSS Framework : Bulma (not yet)

## What you get

...for a blueprint named "demo", you would get the following file structure, with basic wiring in place. For now templates are mostly empty.

````
demo
├── __init__.py
├── demo_controller.py
├── demo_form.py
├── demo_model.py
├── static
│   ├── css
│   │   └── demo-style.css
│   └── js
│       └── demo-script.js
└── templates
    ├── demo-create.html
    ├── demo-index.html
    ├── demo-update.html
    └── demo-view.html

4 directories, 10 files
```
