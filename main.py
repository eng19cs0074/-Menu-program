import os
import subprocess
import docker
import mail
import hosting
	

while(True):
	user = subprocess.getoutput("zenity --info --title 'Menu project' --text 'Which user are you?' --extra-button='Local user' --extra-button='Remote user' --ok-label 'exit' --width=10 --height=100")
	user = user.split()[-2]
	if(user=="Local"):
		while(True):
			ch=subprocess.getoutput("zenity --info --title 'Interface' --text 'How would you like to use the application?' --extra-button='GUI (zenity)' --extra-button='TTS (espeak-ng)' --extra-button='Other options' --ok-label 'exit' --width=10 --height=100")	
			ch = ch.split()[-1]

			if(ch=="(zenity)"):
				while(True):

					x=subprocess.getoutput("zenity --info --title 'Zenity' --text 'Click on the command to execute' --extra-button='date' --extra-button='cal' --extra-button='ls' --extra-button='pwd' --extra-button='man' --extra-button='cat' --extra-button='scp' --ok-label 'exit'  --width=10 --height=100")
					
					choice = x.split()[-1]
					

					if(choice=="date"):
						os.system("date | zenity --text-info")
					elif(choice=="cal"):
						os.system("zenity --calendar")
					elif(choice=="ls"):
						os.system("ls | zenity --text-info")
					elif(choice=="pwd"):
						os.system("zenity --info --text=$(pwd)")	
					elif(choice=="man"):
						os.system("man $(zenity --entry --title='Manual' --text='\t\tEnter the command\n\n') | zenity --text-info --title='Manual'")
					elif(choice=="cat"):
						os.system("cat $(zenity --file-selection --title='Select a file to read') | zenity --text-info")
					elif(choice=="scp"):
						path = subprocess.getoutput("zenity --file-selection --title='Select a file to send'")
						path = path.split()[-1]	
				
						ip = subprocess.getoutput("zenity --entry --title='scp' --text='Enter the IP address\n'")
						ip = ip.split()[-1]
						os.system("scp {} {}:/root".format(path,ip))
						

					else:
						break
					
			elif(ch=="(espeak-ng)"):
				os.system("espeak-ng -s 140 'Welcome'")
				while(True):
					x=subprocess.getoutput("zenity --info --title 'espeak-ng' --text 'Click on the command to execute' --extra-button='date' --extra-button='ls' --extra-button='pwd' --extra-button='man' --extra-button='cat' --extra-button='scp' --ok-label 'exit'  --width=10 --height=100")
					
					choice = x.split()[-1]			
					if(choice=="date"):
						os.system("date | espeak-ng -s 140")
					elif(choice=="ls"):
						os.system("ls | espeak-ng -s 140")
					elif(choice=="pwd"):
						os.system("pwd | espeak-ng -s 140")
					elif(choice=="man"):
						os.system("man $(zenity --entry --title='Manual' --text='\t\tEnter the command\n\n') | espeak-ng -s 140")
					elif(choice=="cat"):	
						os.system("espeak-ng -s 140 'Select a file to read'")
						os.system("cat $(zenity --file-selection --title='Select a file to read') | espeak-ng -s 140")
					elif(choice=="scp"):
						os.system("espeak-ng -s 140 'Select a file to send'")
						path = subprocess.getoutput("zenity --file-selection --title='Select a file to send'")
						path = path.split()[-1]	
						os.system("espeak-ng -s 140 'Enter the IP address'")
						ip = subprocess.getoutput("zenity --entry --title='scp' --text='Enter the IP address\n'")
						ip = ip.split()[-1]
						os.system("espeak-ng -s 140 'Enter the password'")
					
						os.system("scp {} {}:/root".format(path,ip))
						os.system("espeak-ng -s 140 'File sent successfully'")
					else:
						os.system("espeak-ng -s 140 'Thank you'")
						break
			elif(ch=="options"):
				while(True):
					x=subprocess.getoutput("zenity --info --title 'Other options' --text 'What task would you like to perform? \n' --extra-button='Send mail' --extra-button='Start docker' --extra-button='Web hosting' --ok-label 'exit'  --width=10 --height=100")
					choice = x.split()[-1]
					if(choice=="mail"):
						mail.mail()
						
					elif(choice=="docker"):
						while(True):
							x=subprocess.getoutput("zenity --info --title 'Docker' --text 'What would you like to perform? \n' --extra-button='Status' --extra-button='Start service' --extra-button='Images' --extra-button='Containers' --extra-button='Remove' --ok-label 'exit'  --width=10 --height=100")
							stat=subprocess.getoutput("systemctl status docker")
							stat=stat.split()[15]
							choice = x.split()[-1]
							if(choice=="Status"):
								docker.status()
							elif(choice=="service"):
								docker.service(stat)
							elif(choice=="Images"):
								docker.images(stat)
							elif(choice=="Containers"):
								docker.containers(stat)
							elif(choice=="Remove"):
								docker.remove(stat)
							else:
								break
					elif(choice=="hosting"):
						hosting.host()
					else:
						break
			else:
				break

	elif(user=="Remote"):
		ip = subprocess.getoutput("zenity --entry --title='Remote' --text='Enter the IP address'")
		ip = ip.split()[-1]
		print(ip)
		while(True):
			command=subprocess.getoutput("zenity --info --title 'Zenity' --text 'Click on the command to execute' --extra-button='date' --extra-button='cal' --extra-button='ls' --extra-button='cat' --extra-button='run a py program' --ok-label 'exit'  --width=10 --height=100")
			command = command.split()[-1]
			if(command=="date"):
				os.system("ssh {} date".format(ip))
			elif(command=="cal"):
				os.system("ssh {} cal".format(ip))
			elif(command=="ls"):
				os.system("ssh {} ls".format(ip))
			elif(command=="cat"):
				os.system("echo 'Enter the password to see all the files'")
				ls=subprocess.getoutput("ssh {} ls".format(ip))
				ls=ls.split()
				files=" "
				for i in ls:
					if("txt" in i or "py" in i):
						files=files+i+"	"			
				filename=subprocess.getoutput("zenity --entry --title='Read content of file' --text=Select {}".format(files))
				filename=filename.split()[-1]
				os.system("ssh {} cat {}".format(ip,filename))
			elif(command=="program"):
				os.system("echo 'Enter the password to see all the files'")
				ls=subprocess.getoutput("ssh {} ls".format(ip))
				ls=ls.split()
				files=" "
				for i in ls:
					if("py" in i):
						files=files+i+"	"			
				filename=subprocess.getoutput("zenity --entry --title='Run a python program' --text=Select {}".format(files))
				filename=filename.split()[-1]
				if(filename):
					os.system("ssh -X {} python3 {}".format(ip,filename))
				else:
					break
			else:
				break 
		
	else:
		break
			








