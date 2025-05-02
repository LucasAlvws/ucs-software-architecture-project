from jinja2 import Environment, FileSystemLoader
from flask import Blueprint

from app.repositories import RegistrationRepository

upload_bp = Blueprint('upload', __name__)


class RegistrationController:

    def __init__(self):
        self.env = Environment(loader=FileSystemLoader("app/views/"))
        self.repository = RegistrationRepository()

    def get_states_acronym(self):
        template = self.env.get_template("list.jinja")
        acronyms = self.repository.get_states_acronym()
        return template.render(items=acronyms)

    def get_available_years(self):
        template = self.env.get_template("list.jinja")
        years = self.repository.get_available_years()
        return template.render(items=years)

    def get_table(self, filter: dict = {}):
        template = self.env.get_template("table.jinja")

        students = self.repository.get_total_student_count(filter)
        ranking = self.repository.get_course_ranking(filter)

        return template.render(students=students, institutions=ranking)

    def get_modalities(self):
        template = self.env.get_template("list.jinja")
        modalities = self.repository.get_modalities()
        return template.render(items=modalities)
