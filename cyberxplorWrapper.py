import requests
import json
import sys
import urllib3 
urllib3.disable_warnings()

seed = sys.argv[1]
URL = "https://subbuster.cyberxplore.com/api/find"

#do request
r = requests.get(url=URL,timeout=90, verify=False, params={"domain":seed})


if r.status_code == 200:
    
    #raw response
    lol = r.json() 

    #parsing
    for i in range(len(lol["data"])):
        if (lol["data"][i]["subdomain"] is not None):
            print(lol["data"][i]["subdomain"])

else:
    #print("Request Error")
    exit()
exit()

# usage example:
# python3 riddleioWrapper.py github.com
#https://www.domain.com
#http://subdomain.domain.com