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
        sql = text("SELECT DISTINCT(state) FROM registrations;")
        return db.session.execute(sql)

    def get_main_data(self):
        """
        Retorna todos os dados da tela principal. Contendo: 

        Total de alunos matriculados (no Brasil) por ano
        Total de alunos matriculados (no Brasil) por ano, com a possibilidade de escolher a modalidade (EaD ou Presencial)
        Ranking de cursos em 2022 (10 cursos com maior número de matrículas no Brasil)
        Ranking de cursos em 2022 (10 cursos com maior número de matrículas no Brasil), com a possibilidade de escolher a modalidade (EaD ou Presencial)
        Consulta para agregações semelhantes às anteriores com um filtro para Estados
        """        
        return


    def save(self, _object):
        db.session.add(_object)
        db.session.commit()

    def save_dataframe(self, dataframe):
        dataframe.to_sql('registrations', con=db.engine, if_exists='append', index=False)

    def delete(self, _object):
        db.session.delete(_object)
        db.session.commit()
