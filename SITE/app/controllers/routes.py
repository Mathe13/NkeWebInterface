"""Controlar de rotas."""
from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html.j2')

@app.route('/enviacod')
def pageEnviaCode():
    return render_template('send_req.html.j2')