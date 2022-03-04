import requests
import json
import sys
import urllib3 
urllib3.disable_warnings()

seed = sys.argv[1]
URL = "https://sonar.omnisint.io/subdomains/"+seed

#do request
r = requests.get(url=URL,timeout=90, verify=False)


if r.status_code == 200:
    
    #raw response
    lol = r.json()
    lol = list(dict.fromkeys(lol))
    for i in range(len(lol)):
        print(lol[i])

else:
    #print("Request Error")
    exit()
exit()

# res
# out-14.smtp.github.com
# out-15.smtp.github.com
# out-16.smtp.github.com
# out-17.smtp.github.com
# out-18.smtp.github.com
# out-19.smtp.github.com
# out-1.smtp.github.com
# out-20.smtp.github.com
