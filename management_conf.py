import paramiko
hostnames= {"10.85.128.101":"mt701","10.85.128.102":"mt702","10.85.128.103":"mt703","10.85.128.104":"mt704","10.85.128.105":"mt705","10.85.128.106":"mt706","10.85.128.107":"mt707","10.85.128.108":"mt708","10.85.128.109":"mt709","10.85.128.110":"mt710"}
switches=hostnames.keys()
username = "admin"
password = "deeban"
cmd_str1="username labadmin secret labadmin\n"#Add lab admin password
cmd_str2="snmp-server community public rw\n"#Add SNMP community
cmd_str3="management api http-commands\nno shut\n"#Enable EAPI
cmd_str4="ip domain-name blr.aristanetworks.com\n"
#
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for switch in switches:
    	try:
            ssh.connect(switch,22,username,password,look_for_keys=False, allow_agent=False)
            remote_conn = ssh.invoke_shell()				
            print "Enabling required management config in %s" %(switch)
            remote_conn.send("enable\n")
            remote_conn.send("config\n")
            remote_conn.send(cmd_str1)
            remote_conn.send(cmd_str2)
            remote_conn.send(cmd_str3)
            remote_conn.send(cmd_str4)
            remote_conn.send("end\n")
            remote_conn.send("copy running flash:minimal.cfg\n")
            remote_conn.send("write\n")
    
	except:
            print "Connection Failed to %s" %(switch)
        
