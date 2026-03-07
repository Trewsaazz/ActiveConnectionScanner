from ip_threat_scanner.scanner import connection_scanner as cs
from ip_threat_scanner.scanner import ip_lookup as ipl

activeConnections = cs.scanner()


def cli_main():
    for IP in activeConnections:
        IPInfo = ipl.isMalicious(IP)

        # Check if the API returned an error
        if "error" in IPInfo:
            print("Error scanning IP " + str(IP) + ": " + IPInfo["error"] + "\n")
            continue
        
        if IPInfo["data"]["abuseConfidenceScore"] > 10:
            print("\033[1;31m")
        else:
            print("\033[0;32m")
        print("IP Address: " + str(IPInfo["data"]["ipAddress"]))
        print('Malicious score: ' + str(IPInfo["data"]["abuseConfidenceScore"]))
        print('Country: ' + str(IPInfo["data"]["countryCode"]))
        print('Public IP? = ' + str(IPInfo["data"]["isPublic"]))
        print('Probable use: ' + str(IPInfo["data"]["usageType"]))
        print("\033[0;0m")
    print('Total connections scanned: ' + str(len(activeConnections)))


# If you want all info available on the connections comment or delete the previous code and use this one instead

"""
def cli_main():
    for IP in activeConnections: 
        IPInfo = ipl.isMalicious(IP)

        if "error" in IPInfo:
            print("Error scanning IP " + str(IP) + ": " + IPInfo["error"] + "\n")
            continue

        print("IP Address: " + str(IPInfo["data"]["ipAddress"]) + "\n")
        print("Is Public: " + str(IPInfo["data"]["isPublic"]) + "\n")
        print("IP Version: " + str(IPInfo["data"]["ipVersion"]) + "\n")
        print("Is Whitelisted: " + str(IPInfo["data"]["isWhitelisted"]) + "\n")
        print("Abuse Confidence Score: " + str(IPInfo["data"]["abuseConfidenceScore"]) + "\n")
        print("Country Code: " + str(IPInfo["data"]["countryCode"]) + "\n")
        print("Usage Type: " + str(IPInfo["data"]["usageType"]) + "\n")
        print("ISP: " + str(IPInfo["data"]["isp"]) + "\n")
        print("Domain: " + str(IPInfo["data"]["domain"]) + "\n")
        print("Hostnames: " + str(IPInfo["data"]["hostnames"]) + "\n")
        print("Total Reports: " + str(IPInfo["data"]["totalReports"]) + "\n")
        print("Distinct Users Reporting: " + str(IPInfo["data"]["numDistinctUsers"]) + "\n")
        print("Last Reported At: " + str(IPInfo["data"]["lastReportedAt"]) + "\n")
        print("\n")
        print("\n")

    print('Total connections scanned: ' + str(len(activeConnections)) + "\n")
"""
