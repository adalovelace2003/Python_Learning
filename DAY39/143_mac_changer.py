# !/usr/binenv python

import subprocess
import optparse
import re
def welcomeScreen():
    print('''
   _    _    _                    
 /|/|  /_|  / )     / )  /  _      _  _  _ 
/   | (  | (__     (__  /) (/ /)  (/ (- /  
                                 _/        
          ''')

def getArguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface to change its MAC address ")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error(
            "[-] Please specify an interface , use --help for more info ")
    elif not options.new_mac:
        parser.error(
            "[-] Please specify a new mac , use --help for more info ")
    return options


def changeMac(interface, new_mac):
    subprocess.call("ifconfig "+interface + " down ", shell=True)
    print(f"[+] Changing Mac address to {new_mac}...")
    subprocess.call("ifconfig "+interface + " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig "+interface + " up ", shell=True)


def getCurrentMac(interface):
    ifconfig_result = str(subprocess.check_output(["ifconfig", interface]))
    mac_srch_result = re.search(
        r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", (ifconfig_result))
    if mac_srch_result:
        return mac_srch_result.group(0)
    else:
        print("[] Could not read MAC address")

if __name__ == "__main__":
    welcomeScreen()
    options = getArguments()

    currentMac = getCurrentMac(options.interface)
    print(f"Current MAC = {currentMac}")

    changeMac(options.interface, options.new_mac)

    currentMac = getCurrentMac(options.interface)
    if currentMac == options.new_mac:
        print(f"[+] Mac address changed to {options.new_mac} successfully.")
    else:
        print("MAC address did not get changed. ")
