from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import joblib
import numpy as np

app = Flask(__name__)
api = Api(app)

class Predict(Resource):
    def __init__(self):
        self.model = joblib.load('/app/model.pkl')

    def post(self):
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)

        try:
            prediction = self.model.predict(features)
            return jsonify({'prediction': prediction.tolist()})
        except Exception as e:
            return {'error': str(e)}, 400

class Health(Resource):
    def get(self):
        return {'status': 'OK'}, 200

api.add_resource(Predict, '/predict')
api.add_resource(Health, '/health')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)