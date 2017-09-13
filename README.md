# splunk-itsi-alert

usage: itsi_alert -s=splunkhost -p=splunkport -t=splunktoken -o=title -d=description -q=myhostname -x=status[numeric1-5] -z=severity[numeric[1-5] [-l=alertinghoststate -r=alertingcheckcommand -v=true -n=serviceid]
-h Prints the help screen
-s=splunkhost - ip or DNS resolvable name of splunk indexer
-p=splunkport - portnumber for HEC - if in doubt go with 8088
-t=splunktoken - HEC token for notable events
-o=title - Title for Notable Event
-d=description - Description for Notable Event
-q=hostname - Name of the reporting host
-x=status 1-New, 2-In Progress, 3-Pending ...
-z=severity 1-Info, 2-Info, 3-Low ...
-l=state - Optional - can pass in a state for the host
-n=serviceid - Optional - can pass in the ITSI service ID
-r=alertingcheckcommand - Optional - can pass in health check command
-v=true - Optional - verbose output mode

For more details please visit the Notable Events Quickstart Folder in Box
