# ukinflation

A simple app developed as an excuse to use Google App Engine


## How it works

A Cron job scrapes the
[Office for National Statistics](http://www.statistics.gov.uk/cci/nugget.asp?id=19)
for the current value for the
[Retail Price Index](http://en.wikipedia.org/wiki/Retail_Price_Index) and stores it
in the Datastore. The font-end app displays this value, caching it using Memcache
to reduce page load time. Simple


2011 [Steven Wilkin](http://stevenwilkin.com)
