# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return "¡Bienvenido a la Plataforma de Cursos en Línea!"

if __name__ == '__main__':
    app.run(debug=True)

