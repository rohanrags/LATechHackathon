from bs4 import BeautifulSoup
import requests
import urllib.request, json

def scrapper():
    url="http://techfair-data.comparably.com"
    response = requests.get(url)
    links = BeautifulSoup(response.content, "html.parser")
    a = links.find_all('a',href=True)
    print(len(a))
    print(a[0])
    print(a[-1]['href'])

    with open('Data/comp.json', 'w') as fp:
        for company in a:
                if company['href']:
                    with urllib.request.urlopen(company['href']) as url:
                        data = json.loads(url.read().decode())
                        #print(data['culture'])
                        jsonData = {}
                        for key in data['culture']:
                            jsonData[key] = data['culture'][key]['grade']
                        if 'url' in data['company']:
                            jsonData['company_url'] = data['company']['url']
                        print(jsonData)
                        result={}
                        result[data['company']['name']] = jsonData
                        json.dump(result, fp,indent=4)


reviews = scrapper()
#print(reviews)


