
#region import
import requests
import warnings
#endregion import

# CyberArk App ID, Safe, Object
params = {
  'AppID': 'your_App_ID',
  'Safe': 'your_Safe',
  'Object': 'your_Object'
}

password = response.content
input_string = password.decode('utf-8')
print (password.decode('utf-8'))

def Get_CyberArk_Object(params):
  # This will supress any warnings.
  warnings.filterwarnings('ignore')

  #region Variables / Arguments / Parameters
  
  # Certificate & Key
  cert = ('./path/to/client.pem', './path/to/client.key')
  
  headers = {
    'Content-Type': 'Application/json'
  }

  CyberArk_API_URL = 'https://your-cyberark-instance/api/Accounts'
  
  #endregion Variables / Arguments / Parameters

  #region API Request
  
  response = requests.get(CyberArk_API_URL, params=params, headers=headers, cert=cert, verify=False)  

  #endregion API Request

  CyberArk_Object = response.json()

  UserName = {'UserName' : CyberArk_Object['UserName']}

  Password = {'Password' : CyberArk_Object['Content']}

  return(UserName, Password)
