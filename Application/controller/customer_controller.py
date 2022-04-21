from flask import Blueprint

customer = Blueprint("customer", __name__, url_prefix="/customer")

@customer.route("/")
def index():
    return "Welcome to customer view"