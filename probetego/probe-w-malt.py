import subprocess
import MySQLdb
import sys
import datetime

db = MySQLdb.connect(host="localhost",
					user="***",
					passwd="***",
					db="***")

cur = db.cursor()

print"<MaltegoMessage>"
print"<MaltegoTransformResponseMessage>"
print"	<Entities>"

blah = subprocess.check_output(["tshark -n -i mon0 subtype probereq -T fields -e separator= -e wlan.sa -e wlan_mgt.ssid -c 100"], shell=True)
splitblah = blah.split("\n")

for value in splitblah[:-1]:
			splitvalue = value.split("\t")
			MAC = str(splitvalue[1])
			SSID = str(splitvalue[2])
			time = str(datetime.datetime.now())
			#print MAC, SSID
			try:
				cur.execute("REPLACE INTO probes(MAC, SSID, time) VALUES ('%s', '%s', '%s');" % (MAC, SSID, time))
				print"<Entity Type=\"Cam.MAC\">" 
				print"<Value>"+MAC+"</Value>"
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
	
