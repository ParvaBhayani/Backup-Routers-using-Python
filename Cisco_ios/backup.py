from netmiko import ConnectHandler
import getpass
import sys
import time

def backup():

##getting system date 
	day=time.strftime('%d')
	month=time.strftime('%m')
	year=time.strftime('%Y')
	today=day+"-"+month+"-"+year	

##initialising device
	device = {
    		'device_type': 'cisco_ios',
    		'ip': '192.168.1.121',
    		'username': 'xyz',
    		'password': 'abc',
    		'secret':'efg'
    		}

##opening IP file
	ips=open("ip_list.txt")
	print ("Script to take backup of devices, Please enter your credential")
	device['username']=input("Username ")
	device['password']=getpass.getpass()
	print("Enter enable password: ")
	device['secret']=getpass.getpass()

##taking backup
	for line in ips:
		device['ip']=line.strip()
		print("\n\nConnecting Device ",line)
		try:
			net_connect = ConnectHandler(**device)	
		except: 
			print("Something is wrong while connecting device "+device['ip'])
			continue
		net_connect.enable()
		time.sleep(1)
		print ("Reading the running config ")
		output = net_connect.send_command('show run')
		time.sleep(3)
		filename='device_'+device['ip']+'_'+today+".txt"
		saveconfig=open(filename,'w+')
		print("Writing Configuration to file")
		saveconfig.write(output)
		saveconfig.close()
		time.sleep(2)
		net_connect.disconnect()
		print ("Configuration saved to file",filename)
		
	ips.close()
	print ("\nAll device backup completed")


if __name__ == "__main__":
	backup()
