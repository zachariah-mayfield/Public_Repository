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
TableauServerAPI_Version = "3.18"  # replace with your actual version

# Mock functions — replace these with real implementations
def get_tableau_api_token():
    # Call your CyberArk function or Tableau sign-in logic here
    return "your_tableau_auth_token"

def get_tableau_site_id():
    # Call to get Tableau sites and extract the one you need
    return "your_site_id"

# Main function to get Tableau groups
def get_tableau_groups(token, site_id, server_name, environment, api_version):
    try:
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Tableau-Auth": token
        }

        url = f"https://{server_name}.{environment}.Company-Domain.com/api/{api_version}/sites/{site_id}/groups"
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        groups = response.json().get("groups", {}).get("group", [])
        logging.info(f"Retrieved {len(groups)} groups.")
        return groups

    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        sys.exit(1)

# Example usage
Tableau_API_Token = get_tableau_api_token()
Tableau_Site_ID = get_tableau_site_id()
groups = get_tableau_groups(Tableau_API_Token, Tableau_Site_ID, TableauServerName, Environment, TableauServerAPI_Version)

# For testing
# print(groups)
