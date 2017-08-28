import urllib, time, json

#Input Parameters
origin = 'Address A'
destination = 'Address B'
google_api_key = 'xyz'

#prepping parameters
origin = origin.replace(" ","+")
destination = destination.replace(" ","+")
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins='+origin+'&destinations='+destination+'&mode=driving&departure_time=now&key='+google_api_key

#Executing Commute_Time
while True:
    Commute_Time()

#Define Commute_Time
def Commute_Time():
    response = urllib.urlopen(url)
    a = json.loads(response.read())
    temp = a['rows'][0]['elements'][0]['duration_in_traffic']['text'],time.asctime(time.localtime(time.time()))
    #comm_time.append(temp)
    print(temp)
    time.sleep(60)
