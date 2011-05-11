#!/usr/bin/env python

from google.appengine.ext import webapp, db
from google.appengine.ext.webapp import util, template
import os

import models


class MainHandler(webapp.RequestHandler):
	def get(self):
		# retrieve model data
		key = db.Key.from_path('Rpi', '1')
		rpi = db.get(key)

		# render view
		path = os.path.join(os.path.dirname(__file__), 'views', 'index.html')
		self.response.out.write(template.render(path, {'rpi': rpi.value}))


def main():
	application = webapp.WSGIApplication([('/', MainHandler)],
										debug=True)
	util.run_wsgi_app(application)


if __name__ == '__main__':
	main()
