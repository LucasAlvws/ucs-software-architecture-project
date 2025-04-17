from flask import request, jsonify, Blueprint
import pandas as pd
import traceback
from app.repositories import CourseRepository, RegistrationRepository, InstitutionRepository

upload_bp = Blueprint('upload', __name__)


@upload_bp.route('/upload-csv', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nome de arquivo vazio'}), 400

    try:
        course_rep = CourseRepository()
        registration_rep = RegistrationRepository()
        institution_rep = InstitutionRepository()
        df = pd.read_csv(file, sep=';')
        df = df.where(pd.notnull(df), '')
        for index, row in df.iterrows():
            if not row.get('Grau'):
                continue
            institution_dict = {
                'name': row.get('IES').strip(),
                'acronym': row.get('Sigla').strip(),
                'organization': row.get('Organização').strip(),
                'category': row.get('Categoria Administrativa').strip(),
            }
            institution = institution_rep.update_or_create(institution_dict)
            course_dict = {
                'name': row.get('Nome do Curso').strip(),
                'detailed_name': row.get('Nome Detalhado do Curso').strip(),
                'modality': row.get('Modalidade').strip(),
                'degree': row.get('Grau').strip(),
            }
            course = course_rep.update_or_create(course_dict)
            registration_base_dict = {
                'state': row.get('Estado').strip(),
                'city': row.get('Cidade').strip(),
                'institution': institution,
                'course': course,
            }
            for year in df.columns[10:]:
                if not row.get(year):
                    continue
                deafult = {'year': year, 'quantity': row[year]}
                deafult.update(registration_base_dict)
                registration_rep.update_or_create(deafult)  # noqa: F841
        return jsonify({'message': 'CSV recebido com sucesso', 'columns': df.columns.tolist()})
    except Exception as e:
        from IPython import embed;embed(header='')
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500
