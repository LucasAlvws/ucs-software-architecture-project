from app.main import create_app
from jinja2 import Environment, FileSystemLoader
from app.controllers.registration import RegistrationController
from flask import request

app = create_app()

@app.route("/available-years", methods=["GET"])
def years():
    controller = RegistrationController()
    return controller.get_available_years()

@app.route("/table", methods=["GET"])
def table():
    controller = RegistrationController()
    return controller.get_table()

@app.route("/filter", methods=["POST"])
def filter():
    data = request.form.to_dict() or {}

    controller = RegistrationController()
    return controller.get_table(data)

@app.route("/states")
def states():
    controller = RegistrationController()
    return controller.get_states_acronym()

@app.route("/modalities")
def modalities():
    controller = RegistrationController()
    return controller.get_modalities()

@app.route("/")
def home():
    env = Environment(loader=FileSystemLoader("app/views/"))
    template = env.get_template("index.jinja")
    return template.render()

if __name__ == "__main__":
    app.run(debug=True)
