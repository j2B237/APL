from flask import Blueprint

main = Blueprint("main", __name__, url_prefix="/")


# Register controller
from Application.controller import main_controller
from Application.controller import customer_controller
from Application.controller import supplyer_controller
