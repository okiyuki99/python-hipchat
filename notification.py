# coding: utf-8
import json
import requests

# Global Option 
URL=#HIPCHAT URL. Example : "api.hipchat.com"
AUTH_TOKEN=#HIPCHAT TOKEN 
ROOM=#ROOM NAME

# Message Option
CARD_URL=
ID=
TITLE=
ICON_URL=
COLOR=
DESCRIPTION_VALUE=

# Create CONTENT
headers = { 'Content-Type' : 'application/json' }
card = {
  "style": "link",
  "url": CARD_URL,
  "id": ID,
  "title": TITLE,
  "description": {
    "format": "html",
    "value": DESCRIPTION_VALUE 
  },
  "icon": {
    "url": ICON_URL
  }
}
 
data_json = { 'message' : '<b>test1<b>', 'color': COLOR, 'card': card, 'message_format' : 'html' }
params = { 'auth_token' : AUTH_TOKEN }

# POST
r = requests.post('https://'+URL+'/v2/room/'+ROOM+'/notification', data=json.dumps(data_json), headers=headers, params=params)
print(r)
