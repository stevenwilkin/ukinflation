from google.appengine.ext import db

class Rpi(db.Model):
	value = db.StringProperty()
