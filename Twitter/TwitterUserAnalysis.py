from nltk.corpus import stopwords
import sys

s = set(stopwords.words('english'))
m = ("person.fullname", "twitter.friendcount", "network", "twitter.screen-name", "profile_url", "uid", "twitter.id", "person.name", "icon-url", "-")
print"<MaltegoMessage>"
print"<MaltegoTransformResponseMessage>"
print"	<Entities>"
compiled = []
content = sys.argv[2]
hashedcontent = content.replace("#", " ")
equalscontent = hashedcontent.replace("=", " ")
compiled.extend(equalscontent.split())
for value in compiled:
	if value not in s:
		if value not in m:
			clean = str(value).lower().replace("#", "hashtag") 
			print"<Entity Type=\"maltego.Phrase\">" 
			print"<Value>"+str(clean)+"</Value>"
			print"</Entity>"
print"	</Entities>"
print"</MaltegoTransformResponseMessage>"
print"</MaltegoMessage>"
	
