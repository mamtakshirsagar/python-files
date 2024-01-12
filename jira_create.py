# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://mamtakshirsagar11.atlassian.net/rest/api/3/issue"
api_token = "ATATT3xFfGF02mtvHs9Y4vW8pW6PYkBMAoG8TzLf2c7jl9zWJ7fioSnyYhfJRM0sq_BI1cacIszLXn0HsByUA3bPkhDgenzX0ZkQK9jIwYRZhOSNz8RzPSX8lhjm4Ce4VqMZss-b20h0kRMLbmp9VZI3H1bF49ohX0cERrR5mjMtp_TcRh0iWCY=570C9C48"
auth = HTTPBasicAuth("mamtakshirsagar11@gmail.com", api_token)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10010"
    },
    "project": {
      "key":"MAMTAK"
    },
    "summary": "First Jira ticket",
  },
  "update": {}
  
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))