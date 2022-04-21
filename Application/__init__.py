from flask import Flask


# Third party import
from instance.config import config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])

    with app.app_context():
        from Application.controller import main as main_controller
        from Application.controller.customer_controller import customer
        from Application.controller.supplyer_controller import supplyer
        app.register_blueprint(main_controller)
        app.register_blueprint(customer)
        app.register_blueprint(supplyer)

    return app

