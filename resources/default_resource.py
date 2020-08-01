from flask_restful import Resource

class Default(Resource):

	def get(self):
			return {'API use': {
        '/get/original': 'returns a random dialogue from Monty Python\'s Flying Circus',
        'get/new_material': 'returns random a Markov chain generated political speech mixing presidents\' speech with Monty Python\'s dialogue!'
      }
      }