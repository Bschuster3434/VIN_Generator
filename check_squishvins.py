import urllib2
import time

def check_squishvin(svin): ## Checks one single squishVIN and returns yes or no (1 or 0)
	### Known Good Squishvin is 5YJSA1DPCF
	### Below is the url for the Edmunds squish_url
	squish_url = ['https://api.edmunds.com/api/vehicle/v2/squishvins/', '/?fmt=json&api_key=4pgcsw6xmxk6htznkg3bk9d2']
	url = squish_url[0] + str(svin) + squish_url[1]
	
	### Code to handle python exception of urllib2. If not 404, then it's valid.
	try:
		page = urllib2.urlopen(url).read()
		return 1
	except urllib2.HTTPError:
		return 0
		

def check_svinlist(svlist): ##Checks full list of vins and returns paired value list
	paired_vin_list = []
	len_list = len(svlist)
	
	for svin in svlist:
		print "Checking VIN: " + str(svin[1])	
		valid = check_squishvin(svin[1])
		append_list = []
		append_list.append(svin[1])
		for i in svin[0]:
			append_list.append(i)
		append_list.append(valid)	
		paired_vin_list.append(append_list)
		time.sleep(1)
		
	return paired_vin_list