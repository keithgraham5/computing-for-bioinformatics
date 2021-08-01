"""
NAME:          __init__.py
AUTHOR:        Keith Graham  (Lecturer Health Data Science)
EMAIL:         keith.graham5@nhs.et
DATE:          2021
INSTITUTION:   University teaching hospital leeds
DESCRIPTION:   Initialisation file. Creates the Flask application and SQL database
               registers the different modules in the project
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    """Error page to show on page not found (404) error."""
    return render_template('404.html'), 404

# get and register module blueprints
from app.views.controllers import views as views_module
from app.database.controllers import database as database_module

app.register_blueprint(views_module)
app.register_blueprint(database_module)

