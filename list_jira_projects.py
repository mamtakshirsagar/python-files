
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://mamtakshirsagar11.atlassian.net/rest/api/3/project"
API_token="ATATT3xFfGF02mtvHs9Y4vW8pW6PYkBMAoG8TzLf2c7jl9zWJ7fioSnyYhfJRM0sq_BI1cacIszLXn0HsByUA3bPkhDgenzX0ZkQK9jIwYRZhOSNz8RzPSX8lhjm4Ce4VqMZss-b20h0kRMLbmp9VZI3H1bF49ohX0cERrR5mjMtp_TcRh0iWCY=570C9C48"
auth = HTTPBasicAuth("mamtakshirsagar11@gmail.com", API_token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)
complete_response = json.loads(response.text)
#print(type(complete_response))
#print(len(complete_response))
for i in range(len(complete_response)):
    name = complete_response[i]["name"]
    print(name)
#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))