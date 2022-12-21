TeraTerm AutoLauncher
========================

This tool contains 3 custom ttl files used to launch serial, ssh and custom ipv4 
ports automatically.  The user need only install the prerequisite software and 
then populate the csv file with the desired connection information.  An example 
file is included.

Prerequisites
-------------
* Python 3.6+
* Teraterm 4.106
* Create two folders named logs & macros in the teraterm root folder

Download locations
------------------
Python: https://www.python.org/downloads/  
Teraterm: https://osdn.net/projects/ttssh2/releases/  

**Note:**   
All .ttl, .csv and .py files should go into the Teraterm macros directory.  Will it work elsewhere?  Maybe.  I didn't test it elsewhere though.

Usage Example
-------------
	teraterm_macro.py -f teraterm_targets.csv -p C:\util\teraterm-4.106 -l C:\util\teraterm-4.106\logs

The complete invocation syntax is:
	teraterm_macro.py -f csv name -p teraterm app root folder -l log file location  

The csv consists of 7 columns:  
run,connection,target,port,username,password,log_prefix  
  
Descriptions of each column are as follows:  
- run: if set to no the script ignores the connection information
- connection: Must use either serial, ssh, or nossh
- username: leave blank if there is no username
- password: leave blank if there is no password
- log_prefix: this will prepend the log file name (which is date stamped automatically)

Note:  Serial/COM port connections only need 6 entries, see the examples.  I'll fix this for completeness later.  
The first line of the CSV file is ignored.  

**CSV Examples
------------
-<csv>-  
run,connection,target,port,username,password,log_prefix  
yes,serial,19,,,Cisco-COM19-  
yes,ssh,192.168.1.2,22,root,penguinzrule,server2-  
no,nossh,192.168.1.25,23,admin,telnetrockz,server3-  
yes,nossh,192.168.1.25,23,admin,telnetrockz,server3-  
</csv>-  
