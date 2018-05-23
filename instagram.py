from InstagramAPI import InstagramAPI #pip install PythonInstagram
import sys
import json
import requests
try:
	username = sys.argv[1]
except:
	pass
API = InstagramAPI("REPLACE THIS WITH YOUR USERNAME", "REPLACE THIS WITH YOUR PASSWORD")
API.login()
def getID(username):
	API.searchUsername(username)
	return API.LastJson['user']['pk']
def getJson(id):
	url = "https://i.instagram.com/api/v1/users/" + str(id) + "/info/"
	request = requests.get(url)
	return request.json()
def getPicture(json):
	return json["user"]["hd_profile_pic_url_info"]["url"]
ID = getID(username)
json = getJson(ID)
picture = getPicture(json)
print(picture)
