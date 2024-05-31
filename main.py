import requests
import json
import urllib.parse


# Set up the URL
search_url = 'https://slack.com/api/users.lookupByEmail'
message_url = 'https://slack.com/api/chat.postMessage'
message_text = urllib.parse.quote_plus('hello from python')

# Set up the headers
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer xoxb-7227327005184-7197918145526-JcZAixmi2VCATVwr19PW345p'
}


# Make the POST request
response = requests.post(search_url, headers=headers, data={'email': 'pete.letkeman@rakuten.com'}, verify=False)

user_id = None
# Check the response
if response.status_code == 200:
    print('Request successful!')
    print(response.json())
    if not response.json()['ok']:
        print('problem., please check auth header')
    else:
        user_id = (response.json()['user']['id'])
else:
    print('Request failed!')
    print(response.text)

if user_id is not None:
    response = requests.get(message_url + '?channel=' + user_id + '&text=' + message_text, headers=headers, verify=False)
    if response.status_code == 200:
        print('Request successful!')
        print(response.json())
    else:
        print('Request failed!')
        print(response.text)
