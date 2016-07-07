##weather report for n days of specified place using openweathermap.org api
import json
import requests
import sys
import datetime
import pprint
    

##user inputs
city=raw_input("Enter the city name: ")
count=raw_input("Enter the number of days for which you want the weather forecast (<=16): ")
key=raw_input("Enter your api key: ")


##calculating dates
today_date=datetime.datetime.today().date()

##website url
url="http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&units=metric&cnt=%s&APPID=%s" % (city,count,key)

response=requests.get(url)
try:
    response.raise_for_status()
except:
    print "Operation failed!!"
    print "Check your internet connection and/or api credentials "
    sys.exit()
weatherdata=json.loads(response.text)
#pprint.pprint(weatherdata)
print "Weather forecast for "+str(weatherdata['city']['name'])+ ": "
print 

for cnt in xrange(int(count)):
    ##incrementing date
    date_incr=datetime.timedelta(days=cnt)
    print "Date(yyyy-mm-dd) : " + str(today_date+date_incr)
    print "Morning Temperature:"+str(weatherdata['list'][cnt]['temp']['morn'])
    print "Day Temperature:"+str(weatherdata['list'][cnt]['temp']['day'])
    print "Evening Temperature:"+str(weatherdata['list'][cnt]['temp']['eve'])
    print "Night Temperature:"+str(weatherdata['list'][cnt]['temp']['night'])
    print "Minimum Temperature:"+str(weatherdata['list'][cnt]['temp']['min'])
    print "Maximum Temperature:"+str(weatherdata['list'][cnt]['temp']['max'])
    print str(weatherdata['list'][cnt]['weather'][0]['main'])+ " - " + str(weatherdata['list'][cnt]['weather'][0]['description'])
    print "=============================================================="
    print

    
     

