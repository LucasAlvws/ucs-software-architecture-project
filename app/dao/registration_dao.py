from app.main import db
from app.models import Registration
from sqlalchemy import text

class RegistrationDao:
    def __init__(self):
        self.model = Registration

    def get_by_id(self, object_id):
        return self.model.query.get(object_id)

    def get_by_attributes(self, attributes):
        return self.model.query.filter_by(**attributes).first()

    def get_states_acronym(self):
        sql = text("SELECT DISTINCT(state) FROM registration;")
        return db.session.execute(sql)

    def get_modalities(self):
        sql = text("SELECT DISTINCT(course_modality) FROM registration;")
        return db.session.execute(sql)

    def __apply_filter(self, filter: dict = {}):
        if not filter:
            return ""

        sql = " WHERE "
        where_clauses = []
        if int(filter.get('year', '0')):
            where_clauses.append("year = :year")
        if filter.get('mode', 'all') != 'all':
            where_clauses.append("course_modality = :mode")
        if filter.get('state', 'all') != 'all':
            where_clauses.append("state = :state")

        sql += " AND ".join(where_clauses)

        return sql

    def get_course_ranking(self, filter: dict = {}):
        """
        Retorna os 10 cursos com maior número de matrículas. 
        """
        sql = "SELECT institution_name, SUM(student_count) AS students FROM registration"

        sql += self.__apply_filter(filter)

        sql += " GROUP BY institution_name ORDER BY SUM(student_count) DESC LIMIT 10;"
        return db.session.execute(text(sql), filter)

    def get_total_student_count(self, filter: dict = {}):
        """
        Retorna o total de alunos matriculados.
        """
        sql = "SELECT SUM(student_count) AS students FROM registration"
        sql += self.__apply_filter(filter)
        sql += ";"
        return db.session.execute(text(sql), filter)

    def get_available_years(self):
        sql = text("SELECT DISTINCT(year) FROM registration;")
        return db.session.execute(sql)

    def save(self, _object):
        db.session.add(_object)
        db.session.commit()

    def save_dataframe(self, dataframe):
        dataframe.to_sql('registration', con=db.engine, if_exists='append', index=False)

    def delete(self, _object):
        db.session.delete(_object)
        db.session.commit()
