from flask import Flask
from flask_restful import Api
from api import PredictResource, HealthResource

app = Flask(__name__)
api = Api(app)

# Ajouter les ressources à l'API
api.add_resource(PredictResource, '/predict')
api.add_resource(HealthResource, '/health')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')