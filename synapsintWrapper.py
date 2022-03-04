import requests
import json
import sys
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings()



seed = sys.argv[1]
URL = "https://www.synapsint.com/report.php"

#do request
r = requests.post(url=URL,timeout=90, verify=False,data={"search":seed,"btnradio":1})

if r.status_code == 200:
    
    #raw response
    res = r.text
    
    #parsing
    res = res.split("<h2>Subdomains</h2>")[1]
    res = res.split("<h2>Same IP Domains</h2>")[0]

    soup = BeautifulSoup(res, 'html.parser')
    soup = soup.find_all('tbody')
    soup = str(soup[0])

    
    soup = BeautifulSoup(soup, 'html.parser')

    #print(soup)    
    for link in soup.find_all('a'):
        print(link.get('href'))


else:
#     print("Request Error")
    exit()
exit()

# usage example:
# python3 riddleioWrapper.py github.com
# https://gist.github.com
# https://matoom.github.com
# https://partner.github.com
# https://josscrowcroft.github.com
# https://libgit2.github.com
# https://desktop.github.com
# https://pepeiborra.github.com