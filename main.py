from flask import Flask, jsonify
app = Flask('app')
@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({"message": "¡Hola, este es un mensaje de tu API!"})
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)