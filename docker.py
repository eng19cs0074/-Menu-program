import os
import subprocess

def status():

	status=subprocess.getoutput("systemctl status docker")
	status=status.split()[15:22]
	temp = " ".join(status)					
	tem=os.system("zenity --info --text='{}' --title='Status'".format(temp))

def service(stat):
					
	if(stat=="inactive"):
		os.system("systemctl start docker")
		os.system("zenity --info --text='Docker service started' --title='Docker service'")
	else:
		os.system("zenity --info --title='Docker service' --text='Docker is already active'")

def images(stat):
	
	if(stat=="active"):
		img = subprocess.getoutput("docker images")
		img = img.split()[6:]
		i1=0
		i2=1
		i3=2
		string=""
		for i in range(len(img)//7):
			string=string+" " +img[i1]+" "+img[i2]+" "+img[i3]+" "
			i1+=7
			i2+=7
			i3+=7
		image = subprocess.getoutput("zenity --list --title='Images' --text='Select an image below to run OS' --column='REPOSITORY' --column='TAG' --column='IMAGE ID' {}".format(string))
		image = image.split()[-1]
		if(image in string):
			os.system("docker run -it {}".format(image))
		
		
	else:
		os.system("zenity --info --title='Docker images' --text='Docker service is not active'")

def containers(stat):
	
	if(stat=="active"):
		img = subprocess.getoutput("docker ps -a")
		img = img.split()[8:]
		i1=0
		i2=1
		i4=11
		string=""
		for i in range(len(img)//11):
			string=string+" " +img[i1]+" "+img[i2]+" "+" "+img[i4]+" "
			i1+=12
			i2+=12
			i4+=12
		image = subprocess.getoutput("zenity --list --title='Container' --text='Select a container below to launch OS' --column='CONTAINER ID' --column='IMAGE' --column='NAME' {}".format(string))
		
		image = image.split()[-1]
		if(image in string):
			os.system("docker start {}".format(image))
			os.system("docker attach {}".format(image))
	else:
		os.system("zenity --info --title='Docker Container' --text='Docker service is not active'")

def remove(stat):
	
	
	if(stat=="active"):
		img = subprocess.getoutput("docker ps -a")
		img = img.split()[8:]
		i1=0
		i2=1
		i4=11
		string=""
		for i in range(len(img)//11):
			string=string+" " +img[i1]+" "+img[i2]+" "+" "+img[i4]+" "
			i1+=12
			i2+=12
			i4+=12
		image = subprocess.getoutput("zenity --list --title='Container' --text='Select a container below to remove' --column='CONTAINER ID' --column='IMAGE' --column='NAME' {}".format(string))
		
		image = image.split()[-1]
		if(image in string):
			os.system("docker rm {}".format(image))
			
	else:
		os.system("zenity --info --title='Docker' --text='Docker service is not active'")

