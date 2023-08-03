import subprocess
import optparse

print("Mac changer started!")

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="Enter the web interface")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="Enter the your new mac address")

    return parse_object.parse_args()


def change_mac_address(user_interface, user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])

def control_new_mac(interface):
	ifconfig = subprocess.check_output(["ifconfig", interface])
	print(ifconfig)
	
(user_inputs, arguments) = get_user_input()
change_mac_address(user_inputs.interface, user_inputs.mac_address)

print("Your mac address has been successfully changed!")
control_new_mac(user_inputs.interface)
