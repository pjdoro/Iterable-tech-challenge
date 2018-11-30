import pandas as pd
import requests
# read csv into dataframe
data = 'Tomato_data.csv'
df = pd.read_csv(data)
# indicate which records to post based on the row of the data
recs = [0, 1]
users = df.iloc[recs]
# specify target API with Auth placeholders
url = "http://httpbin.org/post"
api_key = '123' #indicate a key
# Create payload for POST request
payload = {}
for x in list(range(0,users.shape[0])):
    row =df.iloc[x]
    payload[str(df.loc[x,'email'])] = [str(x)+ ' : ' +str(row[x]) for x in list(df.columns.values)]
#POST
r = requests.post(url, data=payload)
print(r.text)
