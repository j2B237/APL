
from flask import Blueprint, render_template

supplyer = Blueprint("supplyer", __name__, url_prefix="/supplyer")


@supplyer.route("/")
def index():
    return render_template("supplyer/base.html")
