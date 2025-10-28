from flask import Flask, render_template, request, redirect, url_for, flash, session
import re
 

from flask import Flask, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'una_clave_muy_larga_y_dificil_de_adivinar'

@app.route('/')
def index():
    usuario_activo = session.get('usuario_activo', False)
    return render_template('base.html', usuario_activo=usuario_activo)
    return render_template('base.html')

@app.route('/animal')
def animales():
    usuario_activo = session.get('usuario_activo', False)
    return render_template('animales.html', usuario_activo=usuario_activo)

@app.route('/vehiculos')
def vehiculos():
    usuario_activo = session.get('usuario_activo', False)
    return render_template('vehiculos.html', usuario_activo=usuario_activo)

@app.route('/maravillas')
def maravillas():
    usuario_activo = session.get('usuario_activo', False)
    return render_template('maravillas.html', usuario_activo=usuario_activo)

@app.route('/acerca')
def acerca():
    usuario_activo = session.get('usuario_activo', False)
    return render_template('acercade.html', usuario_activo=usuario_activo)


@app.route('/create', methods=["GET", "POST"])
def crear():
    usuario_activo = session.get('usuario_activo', False)

    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        apellido = request.form.get("apellido", "").strip()
        dia = request.form.get("dia", "")
        mes = request.form.get("mes", "")
        anio = request.form.get("anio", "")
        genero = request.form.get("genero", "")
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        confirmar = request.form.get("confirmar", "")

        if not all([nombre, apellido, dia, mes, anio, genero, email, password, confirmar]):
            flash("Todos los campos son obligatorios.", "danger")
            return render_template("create.html", usuario_activo=usuario_activo)

        if not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúñÑ ]+$", nombre):
            flash("El nombre solo puede contener letras.", "danger")
            return render_template("create.html", usuario_activo=usuario_activo)

        if not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúñÑ ]+$", apellido):
            flash("El apellido solo puede contener letras.", "danger")
            return render_template("create.html", usuario_activo=usuario_activo)

        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            flash("Correo electrónico inválido.", "danger")
            return render_template("create.html", usuario_activo=usuario_activo)

        if password != confirmar:
            flash("Las contraseñas no coinciden.", "danger")
            return render_template("create.html", usuario_activo=usuario_activo)

        flash("Registro exitoso.", "success")
        return redirect(url_for("index"))

    return render_template("create.html", usuario_activo=usuario_activo)


@app.route('/sesion', methods=['GET', 'POST'])
def sesion():
    usuario_activo = session.get('usuario_activo', False)

    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()

        errores = []
        if not email or '@' not in email:
            errores.append("Correo electrónico no válido.")
        if not password:
            errores.append("La contraseña no puede estar vacía.")

        if errores:
            for e in errores:
                flash(e, 'danger')
            return render_template('sesion.html', usuario_activo=usuario_activo)

        session['usuario_activo'] = True
        flash("Inicio de sesión exitoso.", "success")
        return redirect(url_for('index'))

    return render_template('sesion.html', usuario_activo=usuario_activo)

@app.route('/logout')
def logout():
    session.pop('usuario_activo', None)
    flash("Has cerrado sesión correctamente.", "info")
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
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
