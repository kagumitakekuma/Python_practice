import requests

url ="https://api.aokikujira.com/time/get.php"
result =requests.get(url)

print (result.text)
