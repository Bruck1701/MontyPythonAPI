from flask_restful import Resource
from models.sketches import SketchModel
import random
from pymarkovchain import MarkovChain

class NewData(Resource):

	def get(self):
		
		while True:
			index = random.randint(1,45)
			sketch = SketchModel.find_by_index(index)
			text = ' '.join(sketch['dialogue'])
			dialogue_size = len(sketch['dialogue'])
			if dialogue_size > 5:
				break

		if sketch:
			mc = MarkovChain()
			mc.generateDatabase(text)

			result = []
			for line in range(0, dialogue_size):
				result.append(mc.generateString())

			return {'dialogue': result}
		return {'message':'That was completely Different! :('}

	