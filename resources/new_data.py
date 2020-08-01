from flask_restful import Resource
from models.sketches import SketchModel 
from models.speeches import SpeechModel
import random
import markovify


class NewData(Resource):

	def get(self):
		text = ''
		dialogue_size = 0

		while True:
			index = random.randint(1, 45)
			sketch = SketchModel.find_by_index(index)
			text = ' '.join(sketch['dialogue'])
			dialogue_size = len(sketch['dialogue'])
			if dialogue_size > 5:
				break

		index=random.randint(1,1079)
		speech = SpeechModel.find_by_index(index)
		text += speech['body']

		mc = markovify.Text(text)
		mc = mc.compile()
		result = '...'

		for line in range(0, random.randint(10,30)):
			sentence = mc.make_sentence()
			if sentence:
				result+=' '+sentence
		result+='...'

		return {'author':speech['author'],'date':speech['date'],'title':speech['title'],'episode':sketch['sketch'],'new_speech': result}
