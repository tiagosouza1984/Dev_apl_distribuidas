
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

database = {}
database['ALUNO'] = []
database['PROFESSOR'] = []
erro_404 = {'erro':'aluno nao encontrado'}
erro_400 = {'erro':'id ja utilizada'}
erro_400b = {'erro':'aluno sem nome'}
Prof_erro_400a = {'erro':'professor nao encontrado'}
Prof_erro_400b = {'erro':'id ja utilizada'}
Prof_erro_400c = {'erro':'professor sem nome'}


###########################
###########reset##########
###########################
@app.route('/reseta', methods=['POST'])
def reseta_tudo():
    database['ALUNO'] = []
    database['PROFESSOR'] = []
    return "resetado"

###########################
###########ALUNO##########
###########################

@app.route('/alunos')
def alunos():
    return jsonify(database['ALUNO'])

@app.route('/alunos', methods=['POST'])
def novo_aluno():
    novoAluno = request.json
    if 'nome' in novoAluno: 
        for aluno in database['ALUNO']:
            if aluno['id'] == novoAluno['id']:
                return erro_400, 400
            else:
                database['ALUNO'].append(novoAluno)
                return jsonify(database['ALUNO'])
        database['ALUNO'].append(novoAluno)
        return jsonify(database['ALUNO'])   
    else:
        return erro_400b, 400

@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def localiza_aluno(id_aluno):
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
    return erro_404, 404

@app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def edita_aluno(id_aluno):
    edita_nome = request.json
    if 'nome' in edita_nome: 
        for aluno in database['ALUNO']:
            if aluno['id'] == id_aluno:
                aluno['nome'] = edita_nome['nome']
                return jsonify(aluno)
        return erro_404, 404
    else:
        return erro_400b, 400

@app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def deleta_aluno(id_aluno):
    deleta_registro = request.json
    for aluno in database['ALUNO']:
        if aluno['id'] ==id_aluno:
            database['ALUNO'].remove(aluno)
    return erro_404, 404
        
###############################
###########PROFESSOR###########
###############################

@app.route('/professores')
def professores():

    return jsonify(database['PROFESSOR'])

@app.route('/professores', methods=['POST'])
def novo_professor():
    novoProfessor = request.json
    if 'nome' in novoProfessor: 
        for professor in database['PROFESSOR']:
            if professor['id'] == novoProfessor['id']:
                return Prof_erro_400b, 400
            else:
                database['PROFESSOR'].append(novoProfessor)
                return jsonify(database['PROFESSOR'])
        database['PROFESSOR'].append(novoProfessor)
        return jsonify(database['PROFESSOR'])   
    else:
        return Prof_erro_400c, 400

@app.route('/professores/<int:id_professor>', methods=['GET'])
def localiza_professor(id_professor):
    for professor in database['PROFESSOR']:
        if professor['id'] == id_professor:
            return jsonify(professor)
    return Prof_erro_400a, 400

@app.route('/professores/<int:id_professor>', methods=['PUT'])
def edita_professor(id_professor):
    edita_nome = request.json
    if 'nome' in edita_nome: 
        for professor in database['PROFESSOR']:
            if professor['id'] == id_professor:
                professor['nome'] = edita_nome['nome']
                return jsonify(professor)
        return Prof_erro_400a, 400
    else:
        return Prof_erro_400c, 400

@app.route('/professores/<int:id_professor>', methods=['DELETE'])
def deleta_professor(id_professor):
    deleta_registro = request.json
    for professor in database['PROFESSOR']:
        if professor['id'] ==id_professor:
            database['PROFESSOR'].remove(professor)
    return Prof_erro_400a, 400


if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)
