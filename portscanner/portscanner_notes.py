# Socket Bibliothek Importieren 
import socket

# Target IP angeben auf denn der Scann angewendet werden soll (mit user input) 
target = input("Enter your target (IP): ")

# Funktion schreiben um denn Portscanner aufzubauen + einen input (port)
def portscanner(port):
    # try und except um beim durchlaufen eine Meldung zu geben sowie beim fehlschlagen eine "Error" meldung
    try:
        # zuerst deklarieren wir eine Variable in dem der input unseres neuen Socket gespeichert wird 
        # dann erstellen wir einen neuen socket mit (socket.socket) 
        # danach deklariert man eine "family"" in dem fall (AF_INET) da wir nach ipv4 Adressen scannen wollen
        # darauf hin eben so einen "type" (SOCK_STREAM) in anderen worten das der socket über TCP laufen soll 
        # prot=0 ist in diesem fall einfach nur filler da es für SOCK_STREAM nur ein einziges Standardprotokoll gibt 
        ipv4_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        # jetzt nehmen wir unsere variable in denn unser erstellter socket drinnen gespeichert ist und geben .connect((target, port)) an damit der scann weiß auf was er sich schalten soll mit der ip und der port der offen ist 
        ipv4_socket.connect((target, port))
        return True
    except:
        return False

# User input einbauen um die portrange anzugeben + type casting um da input die eingabe zu einen String umwandelt was wir nicht wollen da es eine Zahl seien soll 
port_range_start= int(input("anfang der Port range angeben: "))
port_range_ende = int(input("ende der Port range angeben: "))

# for loop in den der port von oben deklariert wird und bis wie hoch gesucht werden soll ob ports offen sind 
for port in range(port_range_start, port_range_ende, +1):
    # if statement in dem die funktion von oben wiederholt abgefragt wird ob der aktuelle port offen ist 
    if portscanner(port) is True:
        print(f"{port} is open")
    # else statement das wenn der port nicht offen ist das er zum nächsten über gehen soll
    else:
        pass
    # dieser loop wiederholt sich so oft bis die in diesen fall 1000 ports abgeklappert worden 
