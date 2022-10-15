import os
print(50*"x")
print("  _______        _  _______          _ ")
print(" |__   __|      | ||__   __|        | |")
print("    | | ___  ___| |__ | | ___   ___ | |")
print("    | |/ _ \/ __| '_ \| |/ _ \ / _ \| |")
print("    | |  __/ (__| | | | | (_) | (_) | |")
print("    |_|\___|\___|_| |_|_|\___/ \___/|_|")
print("Version: 0.0.3")
print(50*"x"+"\n")
def pingFQDN(host):
    print(70 *"x" + "\n\n OK! Pinging "+ host +" now!. . . \n\n"+ 70 *"x")
    os.system("ping -c 1 " + host)
def dismRepairs():
    print(70 *"x" + "\n\n OK! Running Dism repairs!. . . \n\n"+ 70 *"x")
    os.system("DISM /online /cleanup-image /restorehealth")
def sfcRepairs():
    print(70 *"x" + "\n\n OK! Running SFC repairs!. . . \n\n"+ 70 *"x")
    os.system("sfc /scannow")
def releaseRenew():
    print(70 *"x" + "\n\n OK! Releasing and renewing IP address. . . \n\n"+ 70 *"x")
    os.system("ipconfig /release && ipconfig /renew")
def menu():
    print("What would you like to do?")
    print("1: Ping a specified host")
    print("2: Run DISM repairs on this device")
    print("3: Run SFC repairs on this device")
    print("4: Release and renew the IP address")
    print("5: Exit")
menu()
loop = 1

while loop == 1:
    user_input = input("\nWhat would you like to do? Please make a selection: ")
    if int(user_input) == 1:
        host_select = input("What host would you like to ping? (Please enter FQDN. IE Google.com) ")
        pingFQDN(host_select)
    elif int(user_input) == 2:
        dismRepairs()
    elif int(user_input) == 3:
        sfcRepairs()
    elif int(user_input) == 4:
        releaseRenew()
    elif int(user_input) == 5:
        loop = 0
    print("\n\n")
    menu()









