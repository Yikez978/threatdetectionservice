'''
This script allows control of capture on rpi network tap
@author: devopsec
'''

import subprocess, time, os, re
from datetime import datetime

'''
@summary: 
This class holds functions for Capturing data
'''
class func:
    pcap = None
    
    def enable():            
        ## get datetime for timestamp ##
        dt = datetime.now()
        date = datetime.strftime(dt, '%Y-%m-%d')
        fileOut = "/capture-data/" + date + ".pcap"
        
        #set timer
        t = time.time()
        
        #dump until killed
        pcap = subprocess.Popen(["/usr/sbin/tcpdump -n -e -w "  + fileOut],shell=True)
        while t != 0:
            pcap
	
        return False
    ## end enable function
    
    def disable():
        try:
            check_kill_process("tcpdump")
            return True
        except:
            return False
	
## end killPcap function

    def isRunning():
        ps = subprocess.Popen("ps -eaf | grep /capture-data", shell=True, stdout=subprocess.PIPE)
        output = ps.stdout.readline().decode('ascii')
        try:
            if re.search("pcap",output):
                return True
            else:
                return False
        except:
            return False

def check_kill_process(pstring):
    for line in os.popen("ps ax | grep " + pstring + " | grep -v grep"):
        fields = line.split()
        pid = fields[0]
        os.kill(int(pid), signal.SIGKILL)
