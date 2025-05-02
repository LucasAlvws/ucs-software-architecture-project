# send_csv.py
import requests

url = 'http://localhost:5000/upload-csv'
file_path = 'Matriculados Brasil - Projeto.csv'  # coloque o caminho do seu arquivo aqui

with open(file_path, 'rb') as f:
    files = {'file': (file_path, f, 'text/csv')}
    response = requests.post(url, files=files)

print('Status:', response.status_code)
print('Resposta:', response.json())
