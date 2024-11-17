from flask import Flask, render_template

app = Flask(__name__)

# Ruta para la página inicial
@app.route('/')
def home():
    return render_template('index.html')  # Asegúrate de que este archivo exista en templates

# Ruta para la página de búsqueda de cursos
@app.route('/buscar_cursos')
def buscar_cursos():
    # cursos = [
    #     {"nombre": "Introducción a Python", "descripcion": "Curso básico de Python.", "duracion": "10 horas"},
    #     {"nombre": "Desarrollo Web con Flask", "descripcion": "Aprende a crear aplicaciones web con Flask.", "duracion": "15 horas"},
    #     {"nombre": "Bases de Datos SQL", "descripcion": "Fundamentos y consultas en SQL.", "duracion": "12 horas"},
    #     {"nombre": "Machine Learning Básico", "descripcion": "Primeros pasos en Machine Learning.", "duracion": "20 horas"}
    # ]
    return render_template('buscar_cursos.html')

if __name__ == '__main__':
    app.run(debug=True)

