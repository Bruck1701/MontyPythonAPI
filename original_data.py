from flask_restful import Resource
from models.sketches import SketchModel
import random

class Data(Resource):

	def get(self):
		index = random.randint(1,45)
		sketch = SketchModel.find_by_index(index)
		if sketch:
			
			return sketch
		return {'message':'That was completely Different! :('}

	