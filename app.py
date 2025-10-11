from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')  

    @app.route('/')
def animales():
    return render_template('animales.html')

    @app.route('/')
def vehiculos():
    return render_template('vehiculos.html')

    @app.route('/')
def maravillas():
    return render_template('maravillas.html')

    @app.route('/')
def index():
    return render_template('acercade.html')



    if __name__ == '__main__':
    app.run(debug=True) 