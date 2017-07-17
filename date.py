import datetime
print "IST: " +str(datetime.datetime.now())
print "EST: "+str(datetime.datetime.now() - datetime.timedelta(hours=9,minutes=30))