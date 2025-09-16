import requests
import os
import csv
from dotenv import load_dotenv

#Load API key from .env
load_dotenv()
POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")

limit =1000
url =  f"https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={limit}&sort=ticker&apiKey={POLYGON_API_KEY}"

response = requests.get(url)
data = response.json()
tickers = list()

#collect first batch
for ticker in data['results']:
    tickers.append(ticker)

#handle pagination
while 'next_url' in data:
    print(f"requesting next page: {data['next_url']}")
    response = requests.get(data['next_url']+f'&apiKey={POLYGON_API_KEY}')
    data = response.json()
#handle polygon.io data access limit exception    
    while 'results' in data:
        for ticker in data['results']:
            tickers.append(ticker)
        data={}

#use first ticker as schema reference
fieldnames = list(tickers[0].keys())
output_csv = 'tickers.csv'

#write tickers to csv
with open(output_csv, mode = 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    for t in tickers:
        #ensure missing keys don't break
        row = {key: t.get(key,'') for key in fieldnames}
        writer.writerow(row)

print(f"Wrote {len(tickers)} rows to {output_csv}")
