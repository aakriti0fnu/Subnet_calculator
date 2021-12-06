#!usr/bin/env python3

import sys
import math

def subnet_calc():
     try:
          #Checking Network Address Validity
          while True:
               ip_add = input("\tEnter a valid class-B Network Address: ")
               #We split the network address into individual octets
               ip_octet = ip_add.split('.')
               if (len(ip_octet) == 4) and (128 <= int(ip_octet[0]) <= 191) and (0 <= int(ip_octet[1]) <= 255) and (int(ip_octet[2]) == 0) and (0 == int(ip_octet[3])) :
                    break
               else:
                    print("NOT a valid class-B address.\nPlease re-enter a valid IP\n")
                    continue

          #Checking Number of Hosts Validity
          def no_of_hosts():
                global valid_hosts
                valid_hosts = []
                while True:
                     number_of_hosts = int(input("\tEnter number of subnets required by customer: "))
                     for host in range(number_of_hosts):
                          devices = input("\tEnter number of hosts in subnet # %d: "  % (host+1))
                          valid_hosts.append(devices)
                     #print(valid_hosts)
                     #Maximum number of hosts available in Class-B range would be 2^16
                     max_hosts = pow(2,16) - 2
                     sum = 0
                     for hosts in range(len(valid_hosts)):
                          if (int(valid_hosts[hosts]) <= max_hosts):
                               sum = sum+int(valid_hosts[hosts])
                          else:
                               print("Re-Enter valid number of hosts\n")
                               no_of_hosts()
                     if sum <=max_hosts:
                          print("\n*** All entered number of IP's and Host's are VALID ! ***")
                          break
                     else:
                          print("Re-Enter valid number of hosts")
                          continue
          no_of_hosts()

          
          #Number of network bits (N) is always a constant for class-B IP's
          N = 16
          H = []
          S = []
          M = []
          #Finding number of Host bits (H)
          for host in range(len(valid_hosts)):
               for i in range (16):
                    if ( pow(2,i+1) >= int(valid_hosts[host]) > pow(2,i) ):
                         H.append(i+1)
                         break
          for i in range(len(H)):
               A = 32-( N+int(H[i]) )
               S.append(A)
               M.append(S[i] + N)
        
          #print("Number of Network bits = N = ",N)
          #print("Number of Host bits = H = ",H)
          #print("Number of Subnet bits = S = ",S)
          #print("\tMask bits = M = ",M)

          #Converting Network ID to Binary form
          network_binary = []
          for octet in ip_octet:
               binary_octet = bin(int(octet)).lstrip('0b')
               network_binary.append(binary_octet.zfill(8))
               #print(network_binary)

          binary_ip = "".join(network_binary)
          #print(binary_ip)

          subnet_id = []
          for i in range(len(H)):
               subnet_id.append( binary_ip[:(16+S[i])] + "0" * (H[i]) )
               #print(subnet_id[i])
               binary_ip = binary_ip[:(16+S[i])] + "1" * (H[i])
               #print(binary_ip)
               binary_ip = bin(int(binary_ip, 2)+1).lstrip('0b')
               #print(binary_ip)
               
          
          #Converting everything back to decimal readable format
          #Network ID
          net_ip_octets = []
          for i in range(len(subnet_id)):
               for bit in range(0, 32, 8):
                    net_ip_octet = subnet_id[i][bit : bit + 8]
                    net_ip_octets.append(net_ip_octet)
          #print(net_ip_octets)
          
          net_ip_address = []
          for each_octet in net_ip_octets:
               net_ip_address.append(str(int(each_octet, 2)))

          subnet_network = []
          
          for i in range(0, len(net_ip_address), 4):
               subnet_network.append(".".join(net_ip_address[i:i+4]))

          for host in range(len(subnet_network)):
               print("\n\tSubnet ID of subnet # %d  =>  %s  /  %s" % ( host+1, subnet_network[host], M[host]))

     except KeyboardInterrupt:
          print ("\n\nProgram aborted by user....\nExiting\n")
          sys.exit()

print("\n")
number_of_customers = int(input("Enter number of customers: "))
for customer in range(number_of_customers):
     print("\nCustomer number = ",customer+1)
     subnet_calc()

print("\nThank you for using our Subnet Calculator!!!\n")
