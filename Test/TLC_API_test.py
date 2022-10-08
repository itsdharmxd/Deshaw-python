import requests
from deshaw.qa.httpmods.httputils import constructAuthType
created_session = requests.Session()


payload = {
 "key" : 123,
 "name" : Shubham
}
payload = json.dumps(payload)
response = created_session.post(url, data=payload, headers = {'content-type': "application/json"})

print(response.status_code)
print(response.json())