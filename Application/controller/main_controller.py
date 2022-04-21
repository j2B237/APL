
# Third party import
from flask import render_template

from Application.controller import main


@main.route("/")
def index():
    return render_template("main/base.html")
