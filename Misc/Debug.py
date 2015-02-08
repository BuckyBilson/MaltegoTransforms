import sys

print"<MaltegoMessage>"
print"<MaltegoTransformResponseMessage>"
print"	<Entities>"
x=0
y=0
for value in sys.argv:
	print value
	morevalues = value.split("#")
	for morevalue in morevalues:
		print"<Entity Type=\"maltego.Phrase\">" 
		print"<Value>"+str(morevalue)+" Position:"+str(x)+" HashPosition:"+str(y)+"</Value>"
		print"</Entity>"
		y=y+1
	x=x+1
	y = 0
print"	</Entities>"
print"</MaltegoTransformResponseMessage>"
print"</MaltegoMessage>"
	
