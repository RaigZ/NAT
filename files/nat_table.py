# DO NOT IMPORT ANY OTHER PACKAGES THAT ARE NOT IN THE STANDARD LIBRARY
import random
from typing import Tuple

# CONSTANT USED INSIDE THE UPCOMING NAT PROJECT
# USE THIS <<<<<<<<<<<<<<<<<<
PUBLIC_IP = "172.16.20.2"

# This Class will support both ICMP and TCP packets
## icmp_mapping = NATTable()
## tcp_mapping = NATTable()
## and expose only set(x,y) and get(x,y) functions
class NATTable:
    def __init__(self):
        # NAT translation table
        # ============================ WORK HERE =====================================
        # IMPLEMENT THIS
        self.data = {}
    
    def _random_id(self):
        return random.randint(30001, 65535)

    def set(self, ip_src, id_src) -> Tuple[str, int]:
        # REMEMBER: Create a new random port for each NEW connection else return saved data if source ip and id are found

        # Set WAN side mapping PUBLIC_IP, random_id [range 30,000 - 65,535]
        # ============================ WORK HERE =====================================
        
        '''
        for ip, id in self.data.items(): 
            print("ip_src: " + ip_src)
            print("id_src: " + str(id_src))
            return ip_src, id_src
        else:
        '''
        # NEXT: Make sure that the new_id_src is not in used_ports[]
        new_ip_src = PUBLIC_IP
        new_id_src = self._random_id()
        print("new_id_src = " + str(new_id_src))
        self.data = {(new_ip_src, new_id_src): (ip_src, id_src)}
        print(self.data)

        return new_ip_src, new_id_src

    def get(self, ip_dst, id_dst) -> Tuple[str, int]:
        # Get LAN side mapping ip_src and id_src
        # ============================ WORK HERE =====================================
        #print(self.data)  

        #for self.data in self.data:
            #keys.append(self.data[1]), vals.append(self.data[1])
            #self.data
       
        #keysList = list(self.data.keys())
        
        valsList = list(self.data.values())
        
        #print(keysList)
        #print(valsList)
        #print(valsList[0][0])
        #print("keys : ", str(keys))
        #print("values : ", str(vals))
        #print (self.data[2])

        ip_src = valsList[0][0]
        id_src = valsList[0][1]    
        return ip_src, id_src


# DO NOT MODIFY TEST FUNCTION
def test_datastructure():
    datastructure = NATTable()

    used_ports = []

    computer1_ip = "10.0.0.1"
    computer1_port1 = 33450
    computer1_port2 = 39999

    computer2_ip = "10.0.0.50"
    computer2_port1 = 33450
    computer2_port2 = 34898

    computer3_ip = "10.0.0.120"
    computer3_port1 = 33450
    computer3_port2 = 35255
    computer3_port3 = 36878

    ip_src, port_src = datastructure.set(computer1_ip, computer1_port1)
    used_ports.append(port_src)
    assert ip_src == PUBLIC_IP

    ip_src, port_src = datastructure.get(ip_src, port_src)
    assert ip_src == computer1_ip
    assert port_src == computer1_port1
    
    ip_src, port_src = datastructure.set(computer2_ip, computer2_port1)
    assert ip_src == PUBLIC_IP
    assert port_src not in used_ports
    used_ports.append(port_src)

    ip_src, port_src = datastructure.set(computer2_ip, computer2_port1)
    assert ip_src == PUBLIC_IP
    assert port_src in used_ports

    ip_src, port_src = datastructure.get(ip_src, port_src)
    assert ip_src == computer2_ip
    assert port_src == computer2_port1

    ip_src, port_src = datastructure.set(computer3_ip, computer3_port1)
    assert ip_src == PUBLIC_IP
    assert port_src not in used_ports
    used_ports.append(port_src)

    ip_src, port_src = datastructure.set(computer2_ip, computer2_port2)
    assert ip_src == PUBLIC_IP
    assert port_src not in used_ports
    used_ports.append(port_src)

    for port in used_ports:
        assert port > 30000
    
    ip_src, port_src = datastructure.get(*datastructure.set(computer1_ip, computer1_port2))
    assert ip_src == computer1_ip
    assert port_src == computer1_port2

    ip_src, port_src = datastructure.get(*datastructure.set(computer1_ip, computer1_port2))
    assert ip_src == computer1_ip
    assert port_src == computer1_port2

    ip_src, port_src = datastructure.get(*datastructure.set(computer3_ip, computer3_port2))
    assert ip_src == computer3_ip
    assert port_src == computer3_port2

    ip_src, port_src = datastructure.get(*datastructure.set(computer3_ip, computer3_port3))
    assert ip_src == computer3_ip
    assert port_src == computer3_port3


# THIS IS A PROGRAM TO TEST YOUR IMPLEMENTED DATA STRUCTURE
# THIS PROGRAM MUST NOT CRASH OR SEND ANY ERRORS   
test_datastructure()
print("GOOD JOB :)")
print("Save your data structure for the upcoming NAT project")
