from flask import Flask, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'una_clave_muy_larga_y_dificil_de_adivinar'

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/animal')
def animales():
    return render_template('animales.html')

@app.route('/vehiculos')
def vehiculos():
    return render_template('vehiculos.html')

@app.route('/maravillas')
def maravillas():
    return render_template('maravillas.html')

@app.route('/acerca')
def acerca():
    return render_template('acercade.html')

@app.route('/sesion')
def sesion():
    return render_template('sesion.html')

@app.route('/create', methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        apellido = request.form.get("apellido", "").strip()
        dia = request.form.get("dia", "")
        mes = request.form.get("mes", "")
        anio = request.form.get("año", "")
        genero = request.form.get("genero", "")
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        confirmar = request.form.get("confirmar", "")

        if not nombre or not apellido or not dia or not mes or not anio or not genero or not email or not password or not confirmar:
            flash("Todos los campos son obligatorios.")
            return render_template("create.html", nombre=nombre, apellido=apellido, email=email)

        if not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúñÑ ]+$", nombre):
            flash("El nombre solo puede contener letras.")
            return render_template("create.html", nombre=nombre, apellido=apellido, email=email)

        if not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúñÑ ]+$", apellido):
            flash("El apellido solo puede contener letras.")
            return render_template("create.html", nombre=nombre, apellido=apellido, email=email)

        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            flash("Correo electrónico inválido.")
            return render_template("create.html", nombre=nombre, apellido=apellido, email=email)

        if password != confirmar:
            flash("Las contraseñas no coinciden.")
            return render_template("create.html", nombre=nombre, apellido=apellido, email=email)

        return redirect(url_for("index"))

    return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True)