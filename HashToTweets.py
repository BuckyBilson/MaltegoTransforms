from twitter import *
import os
import sys


token = 'XX'
token_key = 'XX'
con_secret = 'XX'
con_secret_key = 'XX'
t = Twitter(auth=OAuth(token, token_key, con_secret, con_secret_key))

search =sys.argv[1]
count=100

tweets = t.search.tweets(q=search, count=count)
statuses = tweets["statuses"]
print"<MaltegoMessage>"
print"<MaltegoTransformResponseMessage>"
print"	<Entities>"
	
for status in statuses:
	encstatus = status["text"].encode('utf-8')
	print"		<Entity Type=\"maltego.Twit\">"
	print"			<Value>"+encstatus+"</Value>"
	print"			<AdditionalFields>"
	print"				<Field Name=\"content\" DisplayName=\"content\" MatchingRule=\"strict\">"+encstatus+"</Field>"
	print"			</AdditionalFields>"
	print"		</Entity>"

print"	</Entities>"
print"</MaltegoTransformResponseMessage>"
print"</MaltegoMessage>"
	
