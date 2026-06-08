import socket
from time import sleep

target = input("Enter your target (IP): ")

def portscanner(port):
    try:
        ipv4_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        ipv4_socket.connect((target, port))
        return True
    except:
        return False

known_ports = {
    20: "FTP-Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP",
    68: "DHCP Client",
    69: "TFTP",
    80: "HTTP",
    88: "Kerberos",
    110: "POP3",
    123: "NTP",
    135: "MS RPC",
    137: "NetBIOS-NS",
    138: "NetBIOS-DGM",
    139: "NetBIOS-SSN",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP Trap",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    514: "Syslog",
    587: "SMTP Submission",
    631: "IPP",
    636: "LDAPS",
    993: "IMAPS",
    995: "POP3S",
    1433: "MSSQL",
    1521: "Oracle",
    2049: "NFS",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP-Alt",
    8443: "HTTPS-Alt",
    9200: "Elasticsearch",
    27017: "MongoDB"
}

known_port_suche = input("Nach well known ports suchen? (yes or no) ")
if known_port_suche == 'yes':
    print("=================================================")
    print("Well known Port Suche wird gestartet")
    print("=================================================")
    sleep(2)

    for port in known_ports:
        if portscanner(port) is True:
            print(f"Protokoll: {known_ports[port]} Port: {port} is open")

elif known_port_suche == 'no': 
    print("=================================================")
    print("Eigene Port range angeben")
    print("=================================================")
    sleep(2)

    port_range_start = int(input("anfang der Port range angeben: "))
    port_range_ende = int(input("ende der Port range angeben: "))

    print("=================================================")
    print("Eigene Port Suche wird gestartet")
    print("=================================================")
    sleep(2)

    for port in range(port_range_start, port_range_ende):
        if portscanner(port) is True:
            print(f"Port: {port} is open")
