import httplib2
import json
def getgeocode(inputString):
    google_api_key ='AIzaSyBp3vagQ6BvLAa-cBSTvage33vkpo9rcB0'
    locationString = inputString.replace('','+')
    url = ("https://maps.googleapis.com/maps/api/geocode/json?address= %s,CA&key= %s"%(locationString,google_api_key))
    h = httplib2.Http()
    response, content = h.request(url,'GET')
    result = json.loads(content)
    return result
    #print('response header:%s \n\n %response')
#https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY
