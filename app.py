from flask import Flask, jsonify

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API!"}), 200

# Ruta para la página 'about'
@app.route('/about')
def about():
    return jsonify({"version": "1.0", "author": "VM"}), 200

# Ejecutar la aplicación en modo debug
if __name__ == '__main__':
    app.run(debug=True)
