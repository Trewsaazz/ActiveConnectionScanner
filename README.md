## IPNetstatScanner 

This is a python tool to scan active connections in locally and provide some information about the IPs you are connected to and let you know if there is any malicious connections.

## Features

- List active network connections on your machine.
- Query IP addresses in a threat intelligence database.
- Display malicious score and threat rating for each IP.
- Show geolocation information (country/region) of IPs.
- Easy-to-read output suitable for analysts or hobbyists.

## Installation

1. Clone the repository:


git clone 
cd IPNetstatScanner

Install dependencies:



pip install -r requirements.txt
Usage:
You'll need to create a .env file based on the .env-sample to add your API key of abuseIPDB to the code, or directly comment out the API function and use the other one I provided


install the script: 
pip install -e .



then run it:
ipnetstatscanner

The tool will display active connections and threat information for each IP.



## Security Disclaimer
This tool is intended for educational purposes only. Do not use it to scan networks or IPs without proper authorization. Always follow ethical hacking guidelines and your local laws.

License
This project is licensed under the MIT License.
