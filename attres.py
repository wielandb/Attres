import urllib2

def getAddress(lon,lat):
    data = "   "
    radius = 5
    while (len(data) < 5):
        radius = radius + 5
        url = "http://overpass-api.de/api/interpreter?data=%5Bout%3Acsv(name%2C%22addr%3Astreet%22%2C%22addr%3Ahousenumber%22%2C%22addr%3Acity%22%3Bfalse%3B%22%20%22)%5D%5Btimeout%3A25%5D%3B(node%5B%22addr%3Astreet%22%5D(around%3A" + str(radius) + "%2C"+ str(lon) +"%2C%20"+ str(lat) + ")%3B)%3Bout%20body%201%3B"
        response = urllib2.urlopen(url)
        data = response.read()
        #print(radius, data)
    return data, radius
