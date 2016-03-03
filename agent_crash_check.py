import subprocess
import time
import logging
cmd="pidof FocalPointV2"
logging.basicConfig(filename='/var/log/messages',level=logging.DEBUG)
old_pid=int(subprocess.check_output(cmd.split()))
while True:
	new_pid=int(subprocess.check_output(cmd.split()))
	if old_pid!=new_pid:
		print "Focalpoint Has Crashed. Terminating Ribd"
		subprocess.call(['FastCli','-p15','-c','agent rib terminate'])	
        logging.debug("SR55295 FocalPointV2 crashed. RIB agent restarted")
        old_pid=new_pid
	time.sleep(10)
	
