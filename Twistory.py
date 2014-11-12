from twitter import *
import os
import sys


token = 'XXXX'
token_key = 'XXXX'
con_secret = 'XXXX'
con_secret_key = 'XXXX'
t = Twitter(auth=OAuth(token, token_key, con_secret, con_secret_key))

user =sys.argv[1]
x=0
tweets = t.statuses.user_timeline(screen_name=user, count=10000)

print"<MaltegoMessage>"
print"<MaltegoTransformResponseMessage>"
print"<Entities>"
	

for status in tweets:
	encstatus = status["text"].encode('utf-8')
	enctime = status["created_at"].encode('utf-8')
	print"		<Entity Type=\"maltego.Twit\">"
	print"			<Value>"+encstatus+"</Value>"
	print"			<AdditionalFields>"
	print"				<Field Name=\"content\" DisplayName=\"content\" MatchingRule=\"strict\">"+encstatus+"</Field>"
	print"				<Field Name=\"Created_at\" DisplayName=\"created_at\" MatchingRule=\"strict\">"+enctime+"</Field>"
	print"				<Field Name=\"time\" DisplayName=\"content\" MatchingRule=\"strict\">"+encstatus+"</Field>"
	print"				<Field Name=\"content\" DisplayName=\"content\" MatchingRule=\"strict\">"+encstatus+"</Field>"
	print"			</AdditionalFields>"
	print"		</Entity>"
	print status["text"].encode('utf-8')

print"	</Entities>"
print"</MaltegoTransformResponseMessage>"
print"</MaltegoMessage>"
	
