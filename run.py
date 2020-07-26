from flask import Flask, jsonify, request
import json

app = Flask(__name__)

#lista de tarefas
tarefas = [{'id': 0,
            'responsavel': 'Gabriel',
            'tarefa': 'lavar pratos',
            'status': 'pendente'
            },
           {'id': 1,
            'responsavel': 'Giovanna',
            'tarefa': 'varrer casa',
            'status': 'concluido'
            }]


# Lista a tarefa por id e tambem deleta a tarefa
@app.route('/list/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def tarefasFazer(id):
    #imprime na tela uma tarefa pelo id
    if request.method == 'GET':
        try:
            response = tarefas[id]
        except IndexError:
            mensagem = 'Tarefa de ID {} não exixte'.format(id)
            response = {'status': 'ERROR', 'mensagem': mensagem}
        except Exception:
            mensagem = "Erro desconhecido, Procure o ADM da API"
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    #metodo PUT irá atualizar somente o status da tarefa
    elif request.method == 'PUT':
        if tarefas[id]['status'] == 'concluido':
            mensagem = 'ERRO tarefa ja concluida'
            response = {'status': 'erro', 'mensagem': mensagem}
            return jsonify(response)
        elif tarefas[id]['status'] == 'pendente':
            tarefas[id]['status'] = 'concluido'
        return jsonify(tarefas[id])
    #deleta uma tarefa de acordo com o id
    elif request.method == 'DELETE':
        tarefas.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'registro excluido'})


#Lista todas as tarefas, e adiciona as tatefas
@app.route('/list/', methods=['GET', 'POST'])
def list_tarefas():
    #lista todas as tarefas
    if request.method == 'GET':
        return jsonify(tarefas)
    #adiciona uma nova lista
    elif request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao
        tarefas.append(dados)
        return jsonify(tarefas[posicao])


if __name__ == '__main__':
    app.run()
