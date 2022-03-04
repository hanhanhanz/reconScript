import requests
import json
import sys
import urllib3 
urllib3.disable_warnings()

seed = sys.argv[1]
URL = "https://pulsedive.com/api/info.php"

HEADERS = {
    'Host': 'pulsedive.com',
    'Connection': 'close',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
}

QUERY = {'indicator': seed, 'historical': 'true','schema': 1,'pretty': 0}

#get iid
r = requests.get(url=URL,params=QUERY,headers=HEADERS, timeout=10, verify=False)

if r.status_code == 200:
    lol = r.json()
    iid = lol["iid"]
else:
    #print("Not Found")
    exit()

#get response
QUERY2 = {'iid': iid, 'get': 'links','schema': 0,'pretty': 0}
r = requests.get(url=URL,params=QUERY2,headers=HEADERS, timeout=10, verify=False)

#parsing
if r.status_code == 200:
    
    lol = r.json()
    try:
        if len(lol["Active DNS"]) > 0 :
            for i in range(len(lol["Active DNS"])):                
                tes = lol["Active DNS"][i]["summary"]["properties"]["dns"]
                for h in tes.keys():
                    print(tes[h])

    except KeyError:
        pass
    
    try:
        if len(lol["Related Domains"]) > 0 :
            for i in range(len(lol["Related Domains"])):
                print(lol["Related Domains"][i]["indicator"])
    except KeyError:
        pass

    try:
        if len(lol["Related URLs"]) > 0 :
            for i in range(len(lol["Related URLs"])):
                print(lol["Related URLs"][i]["indicator"])
    except KeyError:
        pass
    
else:
    #print("Second Request Error")
    exit()

# usage example:
# python3 riddleioWrapper.py github.com
# https://github.com/SaherBlueEagle/BlueEagle-Endless-RAT/contributors/main/Release/SBEjRAT_Instance.jar
# https://github.com/SaherBlueEagle/BlueEagle-Endless-RAT/commit/d446170a07ca34db7b6e925b4042f998a4303d34/rollup
# https://api.github.com/repos/undefined/undefined
# https://malsup.github.com/jquery.form.js
# https://api.github.com/repos/felixbrucker/foxy-docs/releases/latest
# https://api.github.com/repos/felixbrucker/foxy-docs
# https://api.github.com/repos/Chia-Network/chia-blockchain/releases
# https://github.com/beardage
# http://malsup.github.com/