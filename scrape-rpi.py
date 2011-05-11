#!/usr/bin/env python

import urllib2
import re
from BeautifulSoup import BeautifulSoup

import models


def main():
	# scrape the .gov.uk site
	response = urllib2.urlopen('http://www.statistics.gov.uk/cci/nugget.asp?id=19')
	soup = BeautifulSoup(response.read())

	paragraph = soup.find('p', 'cn_story_subtitle')

	regex = re.compile('RPI (.+%)')
	match = regex.search(str(paragraph))

	# store the RPI value in the datastore
	rpi = models.Rpi(key_name = '1')
	rpi.value = match.group(1)
	rpi.put()

if __name__ == '__main__':
    main()
