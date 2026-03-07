import requests
import os
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter, Retry

load_dotenv()

##Set the API key for abuseipdb in the variable below
API_KEY = os.getenv('API_KEY')

## if you do not want to use the abuse service, you can change it for this one just to obtain the geolocation, you'll need to modify code in the main to use this 
## function instead of the abuse one down below. I recommend using the abuse service, 
## it requires an API key but its free to get in their website https://www.abuseipdb.com/ if you do not want to obtain an API key, this function might be useful


def geoLocate(ip: str) -> dict:
    try:
        r = requests.get(f"https://ip-api.com/json/{ip}", timeout=10)
        r.raise_for_status()
        data = r.json()

        ##Common request errors
    except requests.exceptions.Timeout:
        return {"error": "Request timed out"}
    except requests.exceptions.ConnectionError:
        return {"error": "Network connection error"}
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP error: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Unexpected request error: {str(e)}"}
    except ValueError:
        return {"error": "Invalid JSON received"}
    
    return data


## This is abuseipdb, it requires an API key to use, you can get one for free by signing up on their website. But if you do not wish to get the
## the security information from abuseipdb, you can comment out this function and use the service of your choice.

def isMalicious(ip: str) -> dict:
    try:
        url = "https://api.abuseipdb.com/api/v2/check"
        headers = {
            "Key": API_KEY,
            "Accept": "application/json"
        }
        params = {
            "ipAddress": ip,
            "maxAgeInDays": 100
        }
        rIPDB = requests.get(url, headers=headers, params=params, timeout=10)
        rIPDB.raise_for_status()
        abuseData = rIPDB.json()

    except requests.exceptions.Timeout:
        return {"error": "Request timed out"}
    except requests.exceptions.ConnectionError:
        return {"error": "Network connection error"}
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP error: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Unexpected request error: {str(e)}"}
    except ValueError:
        return {"error": "Invalid JSON received"}
    
    return abuseData

   
