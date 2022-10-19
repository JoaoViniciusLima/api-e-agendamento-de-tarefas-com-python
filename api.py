from flask import  jsonify, request
from agendamentosdb import agendamentos
from flask import Flask

app = Flask(__name__)


# Consultar(todos)
@app.route('/agendamentos',methods=['GET'])
def obter_agendamentos():
    return jsonify(agendamentos)

# Consultar(id)
@app.route('/agendamentos/<int:id>',methods=['GET'])
def obter_agendamento_por_id(id):
    for agendamento in agendamentos:
        if agendamento.get('id') == id:
            return jsonify(agendamentos)
# Editar
@app.route('/agendamentos/<int:id>',methods=['PUT'])
def editar_agendamento_por_id(id):
    agendamento_alterado = request.get_json()
    for indice,livro in enumerate(agendamentos):
        if livro.get('id') == id:
            agendamentos[indice].update(agendamento_alterado)
            return jsonify(agendamentos[indice])
# Criar
@app.route('/agendamentos',methods=['POST'])
def incluir_novo_agendamento():
    novo_agendamento = request.get_json()
    agendamentos.append(novo_agendamento)
    
    return jsonify(agendamentos)
# Excluir
@app.route('/agendamentos/<int:id>',methods=['DELETE'])
def excluir_agendamento(id):
    for indice, agendamento in enumerate(agendamentos):
        if agendamento.get('id') == id:
            del agendamentos[indice]

    return jsonify(agendamentos)