from flask import Flask
from flask_restful import Api
from original_data import Data
from new_data import NewData
from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Data,"/get/original")
api.add_resource(NewData,"/get/new_material")


if __name__ == "__main__":
    
    db.init_app(app)
    app.run(host='0.0.0.0',port=5000, debug=True)
