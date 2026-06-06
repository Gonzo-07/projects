import socket

target = "127.0.0.1"

def portscanner(port):
    try:
        ipv4_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        ipv4_socket.connect((target, port))
        return True
    except:
        return False

for port in range(0, 1000, +1):
    if portscanner(port) is True:
        print(f"{port} is open")
    else:
        pass


# nächste schritte 
#socket-Doku lesen
#Code aufräumen
# Verstehen, warum jede Zeile existiert           

# Verbesserungen
# 1. Implementieren welches protokoll auf welchen port läuft
# 2. user imput ob man nach bestimmten protokollen suchen will oder nach generell offen
# 3. user imput port range einzubauen nach dem er suchen möchte
# 4. Multi threading einbauen


# Notizen
# AF_INET = IPv4
# SOCK_STREAM = TCP
# connect() = versuche Verbindung zu Host:Port
# Erfolg = Port offen
# Exception = Port nicht erreichbar/geschlossen
