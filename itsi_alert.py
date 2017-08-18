import sys
import json
import requests
import uuid
#headers = {'Authorization': 'Splunk 2153AD6D-CB08-4C6D-9B38-15225AD75CB3'}
#splunkserverandport='localhost:8088'
servername=''
port='8088'
token=''
title=''
description=''
status=1
severity=1
hostname=''
hoststate=''
hostcheckcommand=''
hostoutput=''
hostnotes=''
verbose=False
outputarray=[]
def printhelp():
	print "usage: itsi_alert -s=splunkhost -p=splunkport -t=splunktoken -o=title -d=description -x=status[numeric1-5] -z=severity[numeric[1-5] [-l=alertinghoststate -r=alertingcheckcommand -v=true]"
	print "-h Prints the help screen"
	print "-s=splunkhost - ip or DNS resolvable name of splunk indexer"
	print "-p=splunkport - portnumber for HEC - if in doubt go with 8088"
	print "-t=splunktoken - HEC token for notable events"
	print "-o=title - Title for Notable Event"
	print "-d=description - Description for Notable Event"
	print "-x=status 1-New, 2-In Progress, 3-Pending ..."
	print "-z=severity 1-Info, 2-Info, 3-Low ..."
	print "-l=state - Optional - can pass in a state for the host"
	print "-r=alertingcheckcommand - Optional - can pass in health check command"
	print "-v=true - Optional - verbose output mode"
	sys.exit()
def dumpoutput():
	for x in outputarray:
		print x
def constructevent():
	data = {}
	data['event_id'] = str(uuid.uuid4())
	data['title']=title	
	data['description']=description
	data['status']=status
	data['severity']=severity
	if (len(hoststate)>2):
		data['hoststate']=hoststate
	if (len(hostcheckcommand)>2):
		data['hosthealthcheckcommand']=hostcheckcommand
	return data
def log (inputstring):
	if verbose == True:
		outputarray.append(inputstring)
try:
	if (len(sys.argv)>2):	
		for mycounter in range(1,len(sys.argv)):
			if "-s=" in sys.argv[mycounter]:
				servername=str(sys.argv[mycounter][3:])
			if "-p=" in sys.argv[mycounter]:
				try:
					port=str(sys.argv[mycounter][3:])
				except:
					port="8088"
			if "-t=" in sys.argv[mycounter]:
				token=str(sys.argv[mycounter][3:])
			if "-o=" in sys.argv[mycounter]:
				title=str(sys.argv[mycounter][3:])
			if "-d=" in sys.argv[mycounter]:
				description=str(sys.argv[mycounter][3:])
			if "-x=" in sys.argv[mycounter]:
				status=int(sys.argv[mycounter][3:])
			if "-z=" in sys.argv[mycounter]:
				severity=int(sys.argv[mycounter][3:])
			if "-l=" in sys.argv[mycounter]:
				hoststate=str(sys.argv[mycounter][3:])
			if "-r=" in sys.argv[mycounter]:
				hostcheckcommand=str(sys.argv[mycounter][3:])
			if "-v=true" in sys.argv[mycounter]:
				verbose=True
			log ("servername="+servername)
			log ("port="+port)
			log ("token="+token)
			log ("title="+title)
			log ("description="+description)
			log ("status="+str(status))
			log ("severity="+str(severity))
			log ("hoststate="+hoststate)
			log ("hostcheckcommand="+hostcheckcommand)
			
	else:
		print "not enough arguments"
		printhelp()
except:
	print "Exception:"+str(sys.exc_info())
	printhelp()


dumpoutput()
output = constructevent()
payload = {"event": output}
headers = {'Authorization': 'Splunk '+token}
r = requests.post('https://'+servername+":"+str(port)+'/services/collector/event', data=json.dumps(payload), headers=headers, verify=False)
print r.status_code, r.text

