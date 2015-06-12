import urllib2

x = 1
while x == 1:
    response = urllib2.urlopen('http://www.google.com')
    print 'pinging....', response