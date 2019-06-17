#!/usr/bin/env python

from socket import *
import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')



print ("*******************************************")
print ("Port Scanner")
print ("*******************************************")


if __name__ == '__main__':
    targetserver = input('Enter host to scan: ')
    PortLow = input('Enter the first port you would like to scan: ')
    PortHigh = input('Enter the port you would like to stop scanning on: ')
    targetIP = gethostbyname(targetserver)
    print ('Ready to scan : ', targetIP)
    while (PortLow > PortHigh):
        print('ERROR! Please make sure that the first port you wish to scan is less than the last port you would like to scan')
        PortLow = input('Enter the first port you would like to scan: ')
        PortHigh = input('Enter the port you would like to stop scanning on: ')
    #scan reserved ports

    try:
        PortLow = int(PortLow)
        PortHigh = int(PortHigh)
    except ValueError:
        print ("The input string is not a number, it's a string.  Please try again.")

    for i in range(PortLow, PortHigh):
        s = socket(AF_INET, SOCK_STREAM)
        result = s.connect_ex((targetIP, i))
        if(result == 0) :
            print ('Port %d: OPEN' % (i,))
        else:
            print('Port %d: CLOSED' % (i,))    
        s.close()

print ('***********************************************')
print ("Scanning complete")
print ('***********************************************')
