#!/usr/bin/env python

from google.appengine.ext import webapp, db
from google.appengine.ext.webapp import util, template
from google.appengine.api import memcache
import os

import models


def get_rpi():
	# return value from memcache if present
	data = memcache.get('rpi');
	if data is not None:
		return data
	else:
		# retrieve from datastore
		key = db.Key.from_path('Rpi', '1')
		rpi = db.get(key)
        memcache.add('rpi', rpi.value)
        return rpi.value


class MainHandler(webapp.RequestHandler):
	def get(self):
		rpi = get_rpi()
		# render view
		path = os.path.join(os.path.dirname(__file__), 'views', 'index.html')
		self.response.out.write(template.render(path, {'rpi': rpi}))


def main():
	application = webapp.WSGIApplication([('/', MainHandler)],
										debug=True)
	util.run_wsgi_app(application)


if __name__ == '__main__':
	main()
