import requests

url ="https://api.aokikujira.com/time/get.php"
result =requests.get(url)

print ("OK=", result.ok)

if result.ok:
    print("text=", result.text)
print("status_code=",result.status_code)

