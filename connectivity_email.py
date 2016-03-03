import os
import smtplib
SERVER = "prod-mx.aristanetworks.com"
FROM = "sender@blr-lab.com"
TO = ["chetan@arista.com"] # must be a list
SUBJECT = "Lab Status Report"

hostnames= {"10.85.128.101":"mt701","10.85.128.102":"mt702","10.85.128.103":"mt703","10.85.128.104":"mt704","10.85.128.105":"mt705","10.85.128.106":"mt706","10.85.128.107":"mt707","10.85.128.108":"mt708","10.85.128.109":"mt709","10.85.128.110":"mt710"}
switches=hostnames.keys()
down_switches=[]
username = "admin"
password = "deeban"
for switch in switches:
    response = os.system("ping -c 1 " + switch +"> /dev/null 2>&1")
    if response == 0:
        print switch, 'is up!'
    else:
        print switch, 'is down!'
        down_switches.append(switch)
        
TEXT = "This following switches are down " + str(down_switches)
# Prepare actual message
message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail
server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, message)
server.quit()