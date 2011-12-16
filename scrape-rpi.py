#!/usr/bin/env python

from google.appengine.api import memcache
import urllib2
import re
from BeautifulSoup import BeautifulSoup

import models


def main():
	# scrape the .gov.uk site
	response = urllib2.urlopen('http://www.ons.gov.uk/ons/index.html')
	soup = BeautifulSoup(response.read())

	label = soup.find(title="Retail Prices Index").findParent('span')
	value = label.findNextSibling('span').string    # has space at end

	regex = re.compile('(.+%)')
	match = regex.search(str(value))

	# store the RPI value in the datastore
	rpi = models.Rpi(key_name = '1')
	rpi.value = match.group(1)
	rpi.put()

	# flush cached version
	memcache.delete('rpi')

if __name__ == '__main__':
    main()
