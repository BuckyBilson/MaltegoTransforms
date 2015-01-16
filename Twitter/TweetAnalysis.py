from nltk.corpus import stopwords
import sys

s = set(stopwords.words('english'))

print"<MaltegoMessage>"
print"<MaltegoTransformResponseMessage>"
print"	<Entities>"
compiled = []
content = sys.argv[1]
compiled.extend(content.split())
for value in compiled:
	if value not in s:
		clean = str(value).lower().replace("#", "hashtag: ")  
		print"<Entity Type=\"maltego.Phrase\">" 
		print"<Value>"+str(clean)+"</Value>"
		print"</Entity>"
print"	</Entities>"
print"</MaltegoTransformResponseMessage>"
print"</MaltegoMessage>"
	
