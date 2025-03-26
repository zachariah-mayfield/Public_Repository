

import re
import requests
import warnings

# This will supress any warnings.
warnings.filterwarnings('ignore')

headers = {
  'Content-Type': 'Application/json'
}

# CyberArk App ID, Safe, Object
params = {
  'AppID': 'your_App_ID',
  'Safe': 'your_Safe',
  'Object': 'your_Object'
}

# CyberArk API Endpoint
CyberArk_API_URL = 'https://your-cyberark-instance/api/Accounts'

# Certificate & Key
cert = ('./path/to/client.pem', './path/to/client.key')

# Make API Call to Retrieve Password
response = requests.get('https://your-cyberark-instance/api/Accounts', params=params, headers=headers, cert=cert, verify=False)

password = response.content
input_string = password.decode('utf-8')
print (password.decode('utf-8'))
