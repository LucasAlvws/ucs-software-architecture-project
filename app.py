from app.main import create_app
from jinja2 import Environment, FileSystemLoader
from app.controllers.registration import RegistrationController

app = create_app()

@app.route("/available-years")
def years():
    env = Environment(loader=FileSystemLoader("app/views/"))
    template = env.get_template("list.jinja")
    return template.render(items=[2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])

@app.route("/table")
def table():
    env = Environment(loader=FileSystemLoader("app/views/"))
    template = env.get_template("list.jinja")
    return template.render(items=[2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])
    controller = RegistrationController()
    return controller.get_main_data()

@app.route("/states")
def states():
    controller = RegistrationController()
    return controller.get_states_acronym()

@app.route("/")
def home():
    env = Environment(loader=FileSystemLoader("app/views/"))
    template = env.get_template("index.jinja")
    return template.render()

if __name__ == "__main__":
    app.run(debug=True)
