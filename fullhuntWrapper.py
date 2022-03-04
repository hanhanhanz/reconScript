import requests
import json
import sys
import urllib3
import time
urllib3.disable_warnings()

seed = sys.argv[1]
URL = "https://fullhunt.io/api/v1/domain/"+ seed +"/details"

HEADERS = {

    'X-API-KEY': 'APIKEYHERE'
}

def mainreq(URL,HEADERS,seed) :
	#do request
	r = requests.get(url=URL,headers=HEADERS,timeout=300, verify=False)

	if r.status_code == 200:
	    
	    #raw response
	    lol = r.json()

	    #parsing
	    for i in range(len(lol["hosts"])):
	        if (lol["hosts"][i]["tags"] is None):

	            for j in range(len(lol["hosts"][i]["network_ports"])):
	                if lol["hosts"][i]["network_ports"][j] != 80 and lol["hosts"][i]["network_ports"][j] != 443:
	                    tes = lol["hosts"][i]["host"] + ":" + str(lol["hosts"][i]["network_ports"][j])
	                else:
	                    tes = lol["hosts"][i]["host"]
	                print(tes)

	        elif (lol["hosts"][i]["network_ports"] == [80,443] or lol["hosts"][i]["network_ports"]) == [443,80] and ("http" in lol["hosts"][i]["tags"]  or "https" in lol["hosts"][i]["tags"]):
	            tes = lol["hosts"][i]["host"]
	            print(tes)

	        elif ("http" in lol["hosts"][i]["tags"]) or ("https" in lol["hosts"][i]["tags"]):	            
	            for j in range(len(lol["hosts"][i]["network_ports"])):
	                if lol["hosts"][i]["network_ports"][j] != 80 and lol["hosts"][i]["network_ports"][j] != 443:
	                    tes = lol["hosts"][i]["host"] + ":" + str(lol["hosts"][i]["network_ports"][j])
	                else:
	                    tes = lol["hosts"][i]["host"]
	                print(tes)
	        else:
	            pass
	    return 200
	else:
	    return r.status_code
	    
sc = mainreq(URL,HEADERS,seed)

#retry once if fail (sometimes response not 200)
if sc == 504:
	time.sleep(180)
	sc = mainreq(URL,HEADERS,seed)
	exit()
else:
	exit()
	

# usage example:
# python3 riddleioWrapper.py github.com
# cim-data-quality-qa.classroom.github.com
# d.i98.github.com:19
# d.i98.github.com:22
# www.king.github.com
# www.king.github.com
