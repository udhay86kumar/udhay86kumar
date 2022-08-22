import requests
import json

url = "https://api.imagga.com/v2/tags"

#querystring = {"image_url":"https://images.pexels.com/photos/1181403/pexels-photo-1181403.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"}
querystring={"image_url":"https://images.pexels.com/photos/2792025/pexels-photo-2792025.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1 "}
headers = {
    'accept': "application/json",
    'authorization': "Basic YWNjXzY0YjNmYzdmNTdhN2YzMTpmNjg2Zjg5NTllNGI4NTA3N2YzZWMwYTI5ZmRmYTBiYg=="
    }

response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text.encode("ascii"))

for i in range(20):
 tag = data["result"]["tags"][i]["tag"]["en"]
 print(tag)
