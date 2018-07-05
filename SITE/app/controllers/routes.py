"""Controlar de rotas."""
from app import app
from app.controllers import utils
from flask import render_template,request
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html.j2')

@app.route('/enviacod')
def pageEnviaCode():
    return render_template('send_req.html.j2')


@app.route('/cadastrarreq', methods=['POST'])
def cadReq():
    print(request.files['InputArquivo'])
    data={
        'email':request.form['InputEmail'],
        'matricula': request.form['InputMatricula'],
    }
    utils.cadReq(data)

@app.route('/verificar/<campo>/<valor>', methods = ['GET'])
# @app.route('/verificar/')
def verificar(campo,valor):
    # id=request.args.get['id']
    return utils.getReqs(campo,valor)

    # print('teste verificar')


