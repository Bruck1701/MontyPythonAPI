from flask import Flask
from flask_restful import Api
from original_data import Data
from new_data import NewData
from default_resource import Default
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/data2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Default,"/")
api.add_resource(Data,"/get/original")
api.add_resource(NewData,"/get/new_material")
db.init_app(app)

if __name__ == "__main__":
    
    
    app.run(host='0.0.0.0')
