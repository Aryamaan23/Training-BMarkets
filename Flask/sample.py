import requests
import json
url = "https://api.apilayer.com/short_url/hash"

payload = "www.google.com".encode("utf-8")
headers= {
  "apikey": "20dliytiGk0QY1dQsEGE9wnSK3uG8iq9"
}

response = requests.request("POST", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
result=json.loads(result)
#print(json.loads(result))
print(result)
print(result['short_url'])
print(type(result))