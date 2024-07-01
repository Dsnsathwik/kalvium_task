from bs4 import BeautifulSoup
import requests
import csv

URL = "https://results.eci.gov.in/PcResultGenJune2024/index.htm"
res = requests.get(URL)
html_cont = res.content
soup = BeautifulSoup(html_cont, 'html5lib')
# print(soup.prettify())

party_info = soup.find('table', attrs={'class': 'table'}).tbody
# print(party_info.prettify())

all_party_details = []
for party in party_info.findAll('tr'):
    
    party_details = {}
    tds = party.findAll('td')
    
    party_details['name'] = tds[0].text
    party_details['won'] = int(tds[1].a.text)
    party_details['leading'] = int(tds[2].text.strip())
    party_details['total'] = int(tds[3].text)
    
    all_party_details.append(party_details)

# print(len(all_party_details))
with open('./kalvium_task/party_wise_results.csv', 'w') as f:
    w = csv.DictWriter(f, ['name', 'won', 'leading', 'total'])
    w.writeheader()
    for party in all_party_details:
        w.writerow(party)



