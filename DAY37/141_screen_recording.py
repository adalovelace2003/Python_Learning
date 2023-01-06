import subprocess

interface = input("interface > ")
new_mac = input("new MAC > ")  


subprocess.call("ifconfig "+interface+ " down ",shell=True)
print(f"Changing mac address to {new_mac}...")
subprocess.call("ifconfig "+interface+ " hw ether "+ new_mac ,shell=True)
print(f"mac address changed to {new_mac} successfully." )
subprocess.call("ifconfig "+interface+ " up ",shell=True)


