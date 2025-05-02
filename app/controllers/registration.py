import traceback

from jinja2 import Environment, FileSystemLoader
import pandas as pd
from flask import Blueprint, jsonify, request

from app.repositories import RegistrationRepository

upload_bp = Blueprint('upload', __name__)


class RegistrationController:

    def __init__(self):
        self.env = Environment(loader=FileSystemLoader("app/views/"))
        self.repository = RegistrationRepository()

    def get_states_acronym(self):
        template = self.env.get_template("list.jinja")
        acronyms = self.repository.get_states_acronym()
        print("acronyms", acronyms)
        return template.render(items=acronyms)

    def get_main_data(self):
        template = self.env.get_template("list.jinja")
        acronyms = self.repository.get_main_data()
        return template.render(items=acronyms)
