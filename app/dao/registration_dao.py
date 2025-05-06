from app.main import db
from app.models import Registration
from sqlalchemy import text, select, func, desc

class RegistrationDao:
    def __init__(self):
        self.model = Registration

    def get_by_id(self, object_id):
        return self.model.query.get(object_id)

    def get_by_attributes(self, attributes):
        return self.model.query.filter_by(**attributes).first()

    def get_states_acronym(self):
        sql = select(self.model.state).distinct()
        return db.session.execute(sql)

    def get_modalities(self):
        sql = select(self.model.course_modality).distinct()
        return db.session.execute(sql)

    def __apply_filter(self, query, filter: dict = {}):
        if year := int(filter.get('year', '0')):
            query = query.filter_by(year=year)

        if (mode := filter.get('mode', 'all')) != 'all':
            query = query.filter_by(course_modality=mode)

        if (state := filter.get('state', 'all')) != 'all':
            query = query.filter_by(state=state)

        return query

    def get_course_ranking(self, filter: dict = {}):
        """
        Retorna os 10 cursos com maior número de matrículas. 
        """
        sql = select(
            self.model.institution_name,
            func.sum(self.model.student_count).label("students")
        )

        sql = self.__apply_filter(sql, filter)

        sql = (
            sql
            .group_by(self.model.institution_name)
            .order_by(desc(func.sum(self.model.student_count)))
            .limit(10)
        )

        return db.session.execute(sql, filter)

    def get_total_student_count(self, filter: dict = {}):
        """
        Retorna o total de alunos matriculados.
        """
        sql = select(func.sum(self.model.student_count).label("students"))
        sql = self.__apply_filter(sql, filter)
        return db.session.execute(sql, filter)

    def get_available_years(self):
        sql = select(self.model.year).distinct()
        return db.session.execute(sql)

    def save(self, _object):
        db.session.add(_object)
        db.session.commit()

    def save_dataframe(self, dataframe):
        dataframe.to_sql('registration', con=db.engine, if_exists='append', index=False)

    def delete(self, _object):
        db.session.delete(_object)
        db.session.commit()
