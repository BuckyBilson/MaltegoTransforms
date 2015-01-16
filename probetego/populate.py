import subprocess
import MySQLdb
import sys

db = MySQLdb.connect(host="localhost",
					user="****",
					passwd="****",
					db="****")

cur = db.cursor()

print"<MaltegoMessage>"
print"<MaltegoTransformResponseMessage>"
print"	<Entities>"

			#print MAC, SSID
try:
	cur.execute("SELECT MAC FROM probes;")
	MACS = cur.fetchall()
	for value in MACS:
		print"<Entity Type=\"Cam.MAC\">" #You may need to create an SSID entity type in Maltego
		print"<Value>"+str(value[0])+"</Value>"
		print"</Entity>"
except MySQLdb.Error, e:
	print "Error %d: %s" % (e.args[0],e.args[1]) 
	sys.exit(1)


if db:
	db.commit()
	db.close()

print"	</Entities>"
print"</MaltegoTransformResponseMessage>"
print"</MaltegoMessage>"
	
