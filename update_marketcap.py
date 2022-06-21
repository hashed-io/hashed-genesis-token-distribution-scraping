import queue
import pandas as pd
from pycoingecko import CoinGeckoAPI
import json

cg = CoinGeckoAPI()


data = []

with open('data/data.json') as json_file:

    file = json.load(json_file)

    for line in file:
        output = {}

        output["name"] = line['name']
        output["Relay chain"] = line['relay_chain']
        output["Market supply"] = line['market_supply']
        output["Circulation supply"] = line['circulation_supply']
        output["Market cap"] = line['market_cap']

        for k in line["token_distribution"]:
            output[k[0]] = k[1]

        data.append(output)

df = pd.DataFrame(data)
df.fillna(0, inplace=True)

print(df.head(10))

tokens_name = []
queue = []
batch = 50
counter = 0

for i, group in df.groupby("name"):
  if counter < batch:
    counter += 1
    queue.append(i)
  else:
    counter = 0
    queue.append(i)
    tokens_name.append(queue)
    queue = []

updated_data = []
for token_group in tokens_name:
  updated_data.append(cg.get_price(ids='bitcoin', vs_currencies='usd', include_market_cap=True))


