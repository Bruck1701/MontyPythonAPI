from db import db
import random

class SpeechModel(db.Model):

	__tablename__ = 'speeches'

	index = db.Column(db.Integer, primary_key = True)
	author = db.Column(db.String(50))
	body = db.Column(db.String(200000000))
	date = db.Column(db.String(50))
	title = db.Column(db.String(100))

	def __init__(self, author, body, date,title ):
		self.author = author
		self.body = body
		self.date = date
		self.title = title

	@classmethod
	def find_by_index(cls, index):
		result = cls.query.filter_by(index=index).first()
		return {'author':result.author,'body':result.body,'date':result.date,'title':result.title }


