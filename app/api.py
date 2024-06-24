from flask_restful import Resource, reqparse
import pickle
import os

# Charger le modèle
model_path = os.path.join(os.path.dirname(__file__), '../model/model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

class PredictResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('features', type=list, location='json', required=True, help="Features cannot be blank!")
        args = parser.parse_args()

        features = args['features']
        try:
            prediction = model.predict([features]).tolist()
            return {'prediction': prediction}, 200
        except Exception as e:
            return {'error': str(e)}, 400

class HealthResource(Resource):
    def get(self):
        return {'status': 'OK'}, 200
