import ctypes
import sys
import os
import logging
import requests
from datetime import datetime

# Set up logging
log_file = fr"C:\Logs\Tableau_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.info("Script started")

# Admin check
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    logging.info("Restarting script with admin privileges...")
    script = os.path.abspath(sys.argv[0])
    params = " ".join([f'"{arg}"' for arg in sys.argv[1:]])
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}" {params}', None, 1)
    sys.exit()

# Example config values
TableauServerName = "your-tableau-server-name"
Environment = "Development"
TableauServerAPI_Version = "3.18"  # replace with your actual API version

# Mock functions — plug in your real implementations here
def get_tableau_api_token():
    return "your_tableau_auth_token"

def get_tableau_site_id():
    return "your_site_id"

# Get Tableau site settings
def get_tableau_site_settings(token, site_id, server_name, environment, api_version):
    try:
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Tableau-Auth": token
        }

        url = f"https://{server_name}.{environment}.Company-Domain.com/api/{api_version}/sites/{site_id}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        site_info = response.json().get("site", {})

        result = {
            "ExtractEncryptionMode": site_info.get("extractEncryptionMode"),
            "Site_ID": site_id,
            "Site_Name": site_info.get("name")
        }

        logging.info(f"Retrieved site settings: {result}")
        return result

    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        sys.exit(1)

# Example usage
token = get_tableau_api_token()
site_id = get_tableau_site_id()
site_settings = get_tableau_site_settings(token, site_id, TableauServerName, Environment, TableauServerAPI_Version)

# For debugging
# print(site_settings)
