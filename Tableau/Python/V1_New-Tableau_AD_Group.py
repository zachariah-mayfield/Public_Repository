import ctypes
import sys
import os
import logging
import requests
from datetime import datetime

# Setup logging
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
    logging.info("Restarting with admin privileges...")
    script = os.path.abspath(sys.argv[0])
    params = " ".join([f'"{arg}"' for arg in sys.argv[1:]])
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}" {params}', None, 1)
    sys.exit()

# Example values (replace as needed)
TableauServerName = "your-tableau-server-name"
Environment = "Development"
TableauServerAPI_Version = "3.18"
Tableau_Group_Name = "Your-Group-Name"
Tableau_Site_Role = "Viewer"  # or Explorer/Creator

# Mock functions — replace with actual logic
def get_tableau_api_token():
    return "your_tableau_auth_token"

def get_tableau_site_id():
    return "your_site_id"

# Create AD group in Tableau
def new_tableau_ad_group(token, site_id, group_name, site_role, server_name, environment, api_version):
    try:
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Tableau-Auth": token
        }

        url = f"https://{server_name}.{environment}.Company-Domain.com/api/{api_version}/sites/{site_id}/groups"

        payload = {
            "group": {
                "name": group_name,
                "import": {
                    "source": "ActiveDirectory",
                    "domainName": "Company-Domain.com",
                    "grantLicenseMode": "onSync",
                    "siteRole": site_role
                }
            }
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 409:
            logging.warning(f"Group '{group_name}' already exists.")
            print(f"Group '{group_name}' already exists.")
            return None

        response.raise_for_status()
        group_info = response.json().get("group", {})
        logging.info(f"Group created: {group_info}")
        return group_info

    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        sys.exit(1)

# Run the function
token = get_tableau_api_token()
site_id = get_tableau_site_id()
created_group = new_tableau_ad_group(
    token,
    site_id,
    Tableau_Group_Name,
    Tableau_Site_Role,
    TableauServerName,
    Environment,
    TableauServerAPI_Version
)

# Optional print for visibility
# print(created_group)
