from socket import *

print ("*******************************************")
print ("Port Scanner")
print ("*******************************************")

targetserver = input('Enter host to scan: ')
PortLow = input('Enter the first port you would like to scan: ')
PortHigh = input('Enter the port you would like to stop scanning on: ')

targetIP = gethostbyname(targetserver)
print ('Ready to scan : ', targetIP)


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
