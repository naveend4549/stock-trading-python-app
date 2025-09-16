import requests
import os
import csv
from dotenv import load_dotenv
load_dotenv()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
print(f"my api key: {POLYGON_API_KEY}")
limit =1000

url =  f"https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={limit}&sort=ticker&apiKey={POLYGON_API_KEY}"

response = requests.get(url)
data = response.json()

print(data.keys())
tickers = list()
for ticker in data['results']:
    tickers.append(ticker)

while 'next_url' in data:
    print(f"requesting next page: {data['next_url']}")
    response = requests.get(data['next_url']+f'&apiKey={POLYGON_API_KEY}')
    data = response.json()
    print(data)
    while 'results' in data:
        print('******************************************')
        for ticker in data['results']:
            tickers.append(ticker)
        data={}

# print(data)
print(len(tickers))

fieldnames = list(tickers[0].keys())
output_csv = 'tickers.csv'

with open(output_csv, mode = 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    for t in tickers:
        row = {key: t.get(key,'') for key in fieldnames}
        writer.writerow(row)

print(f"Wrote {len(tickers)} rows to {output_csv}")
