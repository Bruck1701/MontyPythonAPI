from db import db
import random

class SketchModel(db.Model):

	__tablename__ = 'scripts'
    
	index = db.Column(db.Integer, primary_key = True)
	episode = db.Column(db.Integer)
	episode_name = db.Column(db.String(100))
	segment = db.Column(db.String(100))
	type = db.Column(db.String(100))
	actor = db.Column(db.String(100))
	character = db.Column(db.String(100))
	detail = db.Column(db.String(100))
	record_date = db.Column(db.DateTime)
	series = db.Column(db.String(100))
	transmission_date = db.Column(db.DateTime)

   
	def __init__(self, episode, episode_name,segment,_type,actor,character,detail,record_date,series,transmission_date ):
		self.episode = episode
		self.episode_name = episode_name
		self.segment = segment
		self._type = _type
		self.actor = actor
		self.character = character
		self.detail = detail
		self.record_date = record_date
		self.series = series
		self.transmission_date = transmission_date


	@classmethod
	def find_by_index(cls, index):
		result = cls.query.filter_by(episode=index).filter_by(type='Dialogue')

		seg_hash={}
		list_sketches=[]
		for el in result.all():
			if el.segment not in seg_hash:
				seg_hash[el.segment] = el.detail
				list_sketches.append(el.segment)
			else:
				seg_hash[el.segment]+='\n'+el.detail

			sketch = list_sketches[random.randint(0,len(list_sketches)-1)]

		return {'episode':el.episode ,'sketch': sketch, 'dialogue': seg_hash[sketch]}
			
