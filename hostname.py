from jsonrpclib import Server
#switches = ["10.85.128.101", "10.85.128.102", "10.85.128.103"]
hostnames= {"10.85.128.101":"mt701","10.85.128.102":"mt702","10.85.128.103":"mt703","10.85.128.104":"mt704","10.85.128.105":"mt705","10.85.128.106":"mt706","10.85.128.107":"mt707","10.85.128.108":"mt708","10.85.128.109":"mt709","10.85.128.110":"mt710"}
switches=hostnames.keys()
username = "admin"
password = "deeban"
def gethostname(switch_ip):
        urlString = "https://{}:{}@{}/command-api".format(username, password, switch_ip) 
        switchReq = Server( urlString ) 
        response = switchReq.runCmds( 1, ["show hostname"] ) 
        hostname=response[0]["hostname"]
        return hostname

def default_hostname(switch_ip):
	urlString = "https://{}:{}@{}/command-api".format(username, password, switch_ip) 
        switchReq = Server( urlString )
        fix_hostname="hostname %s" %hostnames[switch_ip] 
        response = switchReq.runCmds( 1, ["enable","configure",fix_hostname,"end","write"] ) 
        return response

for switch in switches:
    	try:
        	current_hostname=gethostname(switch)
        	if current_hostname!=hostnames[switch]:
            		print "Hostname changed for %s" %(switch)
            		print "Forcing correct hostname %s" %(hostnames[switch])
            		default_hostname(switch)
        	else:
            		print "Hostname has not changed for %s" %(switch)
                                                              
	except:
		print "EAPI not enabled on switch %s" %(switch)
