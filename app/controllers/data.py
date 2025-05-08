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
            }
        )

        year_columns = ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']

        df[year_columns] = df[year_columns].replace('', pd.NA).fillna(0)

        df[year_columns] = df[year_columns].astype(int)

        df = pd.melt(
            df,
            id_vars=[
                "state",
                "city",
                "institution_name",
                "institution_acronym",
                "institution_organization",
                "institution_category",
                "course_name",
                "course_detailed_name",
                "course_modality",
                "course_degree",
            ],
            value_vars=year_columns,
            var_name='year',
            value_name='student_count',
        )

        df = df.where(pd.notnull(df), '')
        registration_rep.update_by_dataframe(df)
        return jsonify({'message': 'CSV recebido com sucesso', 'columns': df.columns.tolist()})

    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500
