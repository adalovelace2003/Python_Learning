import subprocess

interface = input("interface > ")
new_mac = input("new MAC > ")


subprocess.call("ifconfig "+interface+ " down ",shell=True)
print(f"Changing mac address to {new_mac}...")
subprocess.call("ifconfig "+interface+ " hw ether "+ new_mac ,shell=True)
print(f"mac address changed to {new_mac} successfully." )
subprocess.call("ifconfig "+interface+ " up ",shell=True)

''' 
        flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.68  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::b6b2:6104:7629:bf28  prefixlen 64  scopeid 0x20<link>
        ether e0:2a:82:dc:f1:19  txqueuelen 1000  (Ethernet)
        RX packets 733571  bytes 728629821 (694.8 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 517772  bytes 113894444 (108.6 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

'''


