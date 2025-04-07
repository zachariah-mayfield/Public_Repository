import requests
import logging
from datetime import datetime
import ctypes
import sys
import os

# Logging setup
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

# Example config (would be fetched from CyberArk in a full implementation)
Tableau_API_Token = "your_tableau_auth_token"
TableauServerName = "your-tableau-server-name"
Environment = "Development"
TableauServerAPI_Version = "3.18"  # or your actual version

# Get Tableau Sites
def get_tableau_sites(token, server_name, environment, api_version):
    try:
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Tableau-Auth": token
        }

        url = f"https://{server_name}.{environment}.Company-Domain.com/api/{api_version}/sites"
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        sites = data.get("sites", {}).get("site", [])
        logging.info(f"Retrieved {len(sites)} sites.")
        return sites

    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        sys.exit(1)

# Example usage
# sites = get_tableau_sites(Tableau_API_Token, TableauServerName, Environment, TableauServerAPI_Version)
# print(sites)
