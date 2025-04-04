from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Carregar os dados do CSV
df_operadoras = pd.read_csv('C:/Users/Leonardo/Downloads/Relatorio_cadop.csv', on_bad_lines='skip', engine='python')


@app.route('/busca', methods=['GET'])
def buscar_operadoras():
    termo_busca = request.args.get('termo', '')
    resultados = df_operadoras[
        df_operadoras.apply(
            lambda row: termo_busca.lower() in ' '.join(row.astype(str)).lower(), axis=1
        )
    ]
    return jsonify(resultados.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True)
