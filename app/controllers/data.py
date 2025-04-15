from flask import request, jsonify, Blueprint
import pandas as pd

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
        for index, row in df.iterrows():
            from IPython import embed

            embed(header=f'{index}')
            institution_dict = {
                'name': row['IES'].strip(),
                'acronym': row['Sigla'].strip(),
                'organization': row['Organização'].strip(),
                'category': row['Categoria Administrativa'].strip(),
            }
            institution = institution_rep.update_or_create(institution_dict)
            course_dict = {
                'name': row['Nome do Curso'].strip(),
                'detailed_name': row['Nome Detalhado do Curso'].strip(),
                'modality': row['Modalidade'].strip(),
                'degree': row['Grau'].strip(),
            }
            course = course_rep.update_or_create(course_dict)
            registration_base_dict = {
                'state': row['Estado'].strip(),
                'city': row['Cidade'].strip(),
                'institution': institution,
                'course': course,
            }
            registration = registration_rep.update_or_create(registration_base_dict)  # noqa: F841
        return jsonify({'message': 'CSV recebido com sucesso', 'columns': df.columns.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
