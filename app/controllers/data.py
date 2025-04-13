from flask import request, jsonify, Blueprint
import pandas as pd

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/upload-csv', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nome de arquivo vazio'}), 400

    try:
        df = pd.read_csv(file, sep=';')

        # Aqui você pode processar o DataFrame como quiser
        return jsonify({'message': 'CSV recebido com sucesso', 'columns': df.columns.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
