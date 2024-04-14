import subprocess
import optparse
import re

def get_user_inputs():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface", dest="interface", help="Change interface!!")
    parse_object.add_option("-m","--mac", dest="new_mac", help="New mac address")
    return parse_object.parse_args()

def change_mac_address(interface, new_mac):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])

def follow_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    if mac:
        return mac.group(0)
    else:
        return 0

print("""
W     W   EEEEE   L       CCCCC    OOO    M   M   EEEEE  
W  W  W   E       L       C       O   O   MM MM   E      
W W W W   EEEE    L       C       O   O   M M M   EEEE   
W     W   E       L       C       O   O   M   M   E      
W     W   EEEEE   LLLLL   CCCCC    OOO    M   M   EEEEE

""")
print("macChanger starting...")
(user_inputs, arguments) = get_user_inputs()
old_address = follow_new_mac(str(user_inputs.interface))
change_mac_address(user_inputs.interface, user_inputs.new_mac)
final_address = follow_new_mac(str(user_inputs.interface))
if final_address == user_inputs.new_mac and final_address != old_address:
    print("\nCongratulations. MAC address has been changed")
    print("\nOld mac adress: ", old_address)
    print("New mac adress: ", final_address)
else:
    print("ERROR. Something wrong!")    