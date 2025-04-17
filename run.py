from app.main import create_app
from jinja2 import Environment, FileSystemLoader

app = create_app()

@app.route("/available-years")
def years():
    env = Environment(loader=FileSystemLoader("app/templates/"))
    template = env.get_template("list.jinja")
    return template.render(items=[2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])

@app.route("/table")
def table():
    env = Environment(loader=FileSystemLoader("app/templates/"))
    template = env.get_template("table.jinja")
    return template.render(items=["Rafa", "Gab", "Alves", "Stuffs"])

@app.route("/states")
def states():
    env = Environment(loader=FileSystemLoader("app/templates/"))
    template = env.get_template("list.jinja")
    return template.render(items=["RS", "SP", "BH"])

@app.route("/")
def home():
    env = Environment(loader=FileSystemLoader("app/templates/"))
    template = env.get_template("index.jinja")
    return template.render()

if __name__ == "__main__":
    app.run(debug=True)
