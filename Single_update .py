import pandas as pd
import requests
# read csv into dataframe
data = 'Tomato_data.csv'
df = pd.read_csv(data)
# indicate which user to update
rec = 0
row = df.iloc[rec]
# specify target API with Auth placeholders
url = "https://api.iterable.com/api/users/update"
api_key = '123' #indicate a key
# Create payload for POST request
payload =[(x,row[x]) for x in list(df.columns.values)]
print (payload)
#POST
# r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)
# r = requests.post(url, data=payload)
# print(r.text)
