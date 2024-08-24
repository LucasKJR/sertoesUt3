from flask import Flask, render_template
from pymongo import MongoClient
import certifi

app = Flask(__name__)

# Configuração da conexão com MongoDB
uri = "mongodb+srv://user1:l3fBd6rOkevelwXd@sertoesresultados.sdw6b.mongodb.net/?retryWrites=true&w=majority&appName=SertoesResultados"
client = MongoClient(uri, tlsCAFile=certifi.where())
db = client['SertoesResultados']  # Nome do banco de dados
collection = db['Competitors']  # Nome da coleção

@app.route('/')
def index():
    # Puxa apenas os documentos da coleção que pertencem à categoria 'ut2'
    competitors = collection.find({"categoria": "ut2"})
    return render_template('index.html', competitors=competitors)

if __name__ == '__main__':
    app.run(debug=True)
