import urllib2
import cgi
from bs4 import BeautifulSoup
import sys
import time

tarurl = sys.argv[1]
if tarurl[-1] == "/":
	tarurl = tarurl[:-1]
if tarurl[:4] != "http":
	starurl = "http://"+tarurl
else:
	starurl = tarurl
print"<MaltegoMessage>"
print"<MaltegoTransformResponseMessage>"
print"	<Entities>"

url = urllib2.urlopen(starurl).read()
soup = BeautifulSoup(url)
for line in soup.find_all('a'):
	newline = line.get('href')
	try:
		newline = cgi.escape(newline)
		if newline[:4] == "http":
			print"<Entity Type=\"maltego.Domain\">"+"<Value>"+str(newline)+"</Value>"+"</Entity>"
		elif newline[:1] == "/":
			combline = starurl+newline
			print"<Entity Type=\"maltego.Domain\">"+"<Value>"+str(combline)+"</Value>"+"</Entity>"
	except:
		pass
print"	</Entities>"
print"</MaltegoTransformResponseMessage>"
print"</MaltegoMessage>"
