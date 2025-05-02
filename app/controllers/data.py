import traceback

import pandas as pd
from flask import Blueprint, jsonify, request

from app.repositories import RegistrationRepository

upload_bp = Blueprint('upload', __name__)


@upload_bp.route('/upload-csv', methods=['POST'])
def upload_csv():
    registration_rep = RegistrationRepository()

    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nome de arquivo vazio'}), 400

    try:
        df = pd.read_csv(file, sep=';').rename(
            columns={
                'Estado': 'state',
                'Cidade': 'city',
                'IES': 'institution_name',
                'Sigla': 'institution_acronym',
                'Organização': 'institution_organization',
                'Categoria Administrativa': 'institution_category',
                'Nome do Curso': 'course_name',
                'Nome Detalhado do Curso': 'course_detailed_name',
                'Modalidade': 'course_modality',
                'Grau': 'course_degree',
                '2014': 'year_2014',
                '2015': 'year_2015',
                '2016': 'year_2016',
                '2017': 'year_2017',
                '2018': 'year_2018',
                '2019': 'year_2019',
                '2020': 'year_2020',
                '2021': 'year_2021',
                '2022': 'year_2022',
            }
        )
        df = df.where(pd.notnull(df), '')
        registration_rep.update_by_dataframe(df)
        return jsonify({'message': 'CSV recebido com sucesso', 'columns': df.columns.tolist()})
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500
