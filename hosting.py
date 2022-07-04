import os
import subprocess

def host():
	path = subprocess.getoutput("zenity --file-selection --title='Select html file to host'")
	path = path.split()[-1]
	if(".html" in path):
		
		os.system("cp {} /var/www/html".format(path))
		ip= subprocess.getoutput("ifconfig enp0s3")
		ip=ip.split()[5]
		file_name=path.split('/')[-1]
		os.system("zenity --info --text='Succesfully hosted website. visit {}/{}' --title='Web hosting' --width=200".format(ip,file_name))
	else:
		os.system("zenity --error --text='Selected file is not a html file'")
		
	

