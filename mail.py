import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
import os
import subprocess

def mail():
	email = 'chethanrao5355@gmail.com'
	password = 'bdgepsyvfhltqzit'

	send_to_email = subprocess.getoutput("zenity --entry --title='EMAIL' --text='Send email to - \n'")
	send_to_email = send_to_email.split()[-1]
	subject =  subprocess.getoutput("zenity --entry --title='EMAIL' --text='Subject: \n'")
	res = subject.split()
	subject = ""
	for i in range(11,len(res)):
		subject=subject+res[i]+" "

	message = subprocess.getoutput("zenity --entry --title='EMAIL' --text='Body: \n'")
	res = message.split()
	message = ""
	for i in range(11,len(res)):
		message=message+res[i]+" "

	ch=subprocess.getoutput("zenity --info --title 'EMAIL' --text 'Do you want to attach a file?\n' --extra-button='yes' --ok-label 'no' --width=10 --height=100")	
	ch = ch.split()[-1]

	msg = MIMEMultipart()

	if(ch=="yes"):
		file_location = subprocess.getoutput("zenity --file-selection --title='Attach a file'")
		file_location = file_location.split()[-1]	

		filename = os.path.basename(file_location)
		attachment = open(file_location, "rb")
		part = MIMEBase('application', 'octet-stream')
		part.set_payload(attachment.read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

		msg.attach(part)

	msg['From'] = email
	msg['To'] = send_to_email
	msg['Subject'] = subject

	msg.attach(MIMEText(message, 'plain'))

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(email, password)
	text = msg.as_string()
	server.sendmail(email, send_to_email, text)
	server.quit()
	os.system("zenity --info --title='EMAIL' --text='Mail sent successfully'")
