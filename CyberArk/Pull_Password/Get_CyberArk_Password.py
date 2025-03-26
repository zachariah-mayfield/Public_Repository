
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

# Certificate & Key
cert = ('./path/to/client.pem', './path/to/client.key')

def Get_CyberArk_Object(params, cert):
  # This will supress any warnings.
  warnings.filterwarnings('ignore')
  #region Variables / Arguments / Parameters
  headers = {
    'Content-Type': 'Application/json'
  }
  # CyberArk API URL
  CyberArk_API_URL = 'https://your-cyberark-instance/api/Accounts'
  #endregion Variables / Arguments / Parameters
  #region API Request
  response = requests.get(CyberArk_API_URL, params=params, headers=headers, cert=cert, verify=False)  
  #endregion API Request
  CyberArk_Object = response.json()
  
  UserName = {'UserName' : CyberArk_Object['UserName']}
  Password = {'Password' : CyberArk_Object['Content']}
  
  return(UserName, Password)

CyberArk_Object = Get_CyberArk_Object(params, cert)
