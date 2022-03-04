import requests
import json
import sys
import urllib3 
urllib3.disable_warnings()

seed = sys.argv[1]
URL = "https://riddler.io/search/exportcsv"

#do request
r = requests.get(url=URL,timeout=90, verify=False, params={"q":"pld:"+seed})


if r.status_code == 200:
    
    #raw response
    lol=r.text
    #lol = r.json()
    lol = lol.split("\n")
    
    #parsing
    for i in range(2,len(lol)-1):
        print(lol[i].split(",")[5])
else:
    #print("Request Error")
    exit()
exit()

# usage example:
# python3 riddleioWrapper.py github.com
# gbarnett.github.com                                                                                               
# nao58.github.com                                                                                                  
# travlr.github.com                                                                                                 
# qetzal.github.com                                                                                                 
# kwarc.github.com                                                                                                  
# trisweb.github.com                                                                                                
# salencebg.github.com                                                                                              
# swordapp.github.com
# rcmdnk.github.com
# rdallasgray.github.com

