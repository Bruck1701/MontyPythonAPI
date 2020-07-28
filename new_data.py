from flask_restful import Resource
from models.sketches import SketchModel
import random
import markovify


class NewData(Resource):

	def get(self):
		text=''
		dialogue_size=0

		for i in range(5):
			index = random.randint(1,45)
			sketch = SketchModel.find_by_index(index)
			text += ' '.join(sketch['dialogue'])
			dialogue_size += len(sketch['dialogue'])
		
		mc = markovify.Text(text)
		mc = mc.compile()

		result = []
		for line in range(0, random.randint(1,dialogue_size-1)):
			sentence = mc.make_sentence()
			if sentence:
				result.append(sentence)

		return {'dialogue': result}
		
		

	