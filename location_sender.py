import urllib3
import json
import requests
from twilio.rest import Client #for text messaging.

http = urllib3.PoolManager()
r = http.request('GET', 'http://ipinfo.io/json')
data = json.loads(r.data.decode('utf-8'))
city=data['city']
loc=data['loc']
print(city,loc)
sid= "your twilio account sid"
token= "your twilio auth token"
client = Client(sid, token)
client.messages.create(to="Receiver contact number",
                       from_="Sender contact number",
body="Hello,I am in  "+city+"   and my location cordinates are  " +loc)
