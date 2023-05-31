from flask import Flask, make_response, jsonify , request
from bd import carros


app = Flask(__name__)
 
app.config['JSON_SORT_KEYS'] = False 


@app.route('/carros', methods=['GET'])
def get_carros(): 
    return make_response(
        jsonify(
            carros))


@app.route('/carros', methods=['POST']) 
def create_carro():
    carro = request.json
    carros.append(carro) # type: ignore
    return carro


app.run()