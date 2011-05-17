# ukinflation

A simple app developed as an excuse to use Google App Engine


## How it works

A Cron job scrapes the
[Office for National Statistics](http://www.statistics.gov.uk/cci/nugget.asp?id=19)
for the current value for the
[Retail Price Index](http://en.wikipedia.org/wiki/Retail_Price_Index) and stores it
in the Datastore

The front-end app uses the built-in webapp framework and displays this retrieved
value, caching it via Memcache to reduce page load time

Simple


## API

A basic JSON API is exposed at `/rpi.json`


2011 [Steven Wilkin](http://stevenwilkin.com)
