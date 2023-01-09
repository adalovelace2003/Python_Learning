# !/usr/binenv python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address ")
parser.add_option("-m", "--mac", dest="new_mac", help="New Mac address")


(options,arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac


subprocess.call("ifconfig "+interface + " down ", shell=True)
print(f"Changing mac address to {new_mac}...")
subprocess.call("ifconfig "+interface + " hw ether " + new_mac, shell=True)
print(f"mac address changed to {new_mac} successfully.")
subprocess.call("ifconfig "+interface + " up ", shell=True)
