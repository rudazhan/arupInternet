"""Never lose internet at Arup.

Throw this code into python to never lose internet (hopefully!)

ARUP LAD network
WiFi: nyquist-guest
username: visitor.wireless
password: 2ndavenue
"""

import urllib2

x = 1
while x == 1:
    response = urllib2.urlopen('http://www.google.com')
    print 'pinging....', response
