import requests
import urllib, json
url = "https://apiv2.gofile.io/getServer"
response = requests.get(url)
print(response)
jsonResponse = response.json()
print(jsonResponse['data']['server'])
server_url = str(jsonResponse['data']['server'])
url = "https://" + "srv-file7" + ".gofile.io/upload"

files={'file': open('hello.txt', 'rb')}

post_response = requests.post(url,filesUploaded=files)
get_response = requests.get(url)
# jsonResponse = get_response.json()
print(get_response)