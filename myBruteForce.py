import requests
from requests.structures import CaseInsensitiveDict

url = "todo"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = 'todo'
print(data)
r = requests.post(url, headers=headers, data=data, timeout=10)
if r.status_code == 200:
    print("Success")

# Basic
print(r.status_code)
print(r.text)

# JSON body (if response is JSON)
try:
    print(r.json())
except ValueError:
    print("Response not JSON")

# Full debug: headers and raw bytes
print("Response headers:", r.headers)
print("Raw bytes:", r.content)
