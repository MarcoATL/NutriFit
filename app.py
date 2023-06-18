from flask import Flask, render_template
from flask import jsonify
import json
from flask import Flask
from flask import request,redirect,url_for, session
from BaseDatos import verificar_credenciales, obtener_usuario_por_correo, actualizar_usuario

app = Flask(__name__)
app.secret_key = 'una clave secreta muy segura'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nutrifit')
def main():
    if 'usuario' in session:
        correo = session['usuario']
        usuario = obtener_usuario_por_correo(correo)
        return render_template('NutriFit.html', usuario=usuario)
    else:
        return redirect(url_for('index'))

@app.route('/platillos')
def obtener_platillos():
    with open('static/platillos.json', 'r') as file:
        platillos = json.load(file)
    return jsonify(platillos)

@app.route('/actualizar_datos', methods=['POST'])
def actualizar_datos():
    if 'usuario' in session:
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        correo = request.form['correo']
        actualizar_usuario(nombre, apellidos, correo)
        return redirect(url_for('main'))  # Redireccionar de vuelta a la página principal después de actualizar los datos.
    else:
        return redirect(url_for('index'))  # Redirigir al usuario a la página de inicio de sesión si no ha iniciado sesión.


@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    correo = request.form['correo']
    contrasena = request.form['contrasena']
    
    if verificar_credenciales(correo, contrasena):
        # Credenciales válidas, redirigir a la página NutriFit.html
        session['usuario'] = correo
        return redirect(url_for('main'))
    else:
        # Credenciales inválidas, mostrar mensaje de error en la página index.html
        return render_template('index.html', error='Credenciales inválidas')

@app.route('/cerrar_sesion')
def cerrar_sesion():
    # Eliminar 'usuario' de la sesión si está presente
    session.pop('usuario', None)
    
    # Redirigir al usuario a la página de inicio
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
