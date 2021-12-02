################################################################################
#
#READ THE COMMENTS BEFORE RUNNING
#Run:		teraterm_macro.py -f teraterm_targets.csv -p C:\util\teraterm-4.106 -l C:\util\teraterm-4.106\logs
#File:      teraterm_macro.py
#Date:      2021NOV23
#Author:    William Blair
#Contact:	williamblair333@gmail.com
#Tested on: Windows 10 21H1
#
#This script is intended to do the following:
#
#-automate launching teraterm terminal session via input csv file
#-See attached 'teraterm_connections.csv' file for examples
#-Automate log creation under 'filepath\logs
#-One command to launch all sessions
################################################################################

import argparse, csv, sys, time
from subprocess import call
#################################################################################

parser = argparse.ArgumentParser(description='To set directory and source file')

parser.add_argument('-f', '--file', type=str, help='Teraterm sessions config' + \
'file,\t Required', required=True)

parser.add_argument('-p', '--path', type=str, help='Teraterm sessions path ' + \
'to config file,\t Required', required=True)

parser.add_argument('-l', '--logpath', type=str, help='Teraterm sessions log' + \
'file location,\t Required', required=True)

args = parser.parse_args()

filename = (args.file)
filepath = (args.path)
logpath  = (args.logpath)

#Need a delay between each launch of the ttpmacro.exe or script errors may occur
sec = 1
#################################################################################

#Get filepath and logpath from command line arguments
#This will build the commands that need to run for each session entry

teralog         = logpath + '\\'
teraold         = teralog + 'old'
teramacro_ser   = filepath + '\\ttpmacro.exe macros\\console.ttl'
teramacro_ssh   = filepath + '\\ttpmacro.exe macros\\ssh.ttl'
teramacro_nossh = filepath + '\\ttpmacro.exe macros\\nossh.ttl'
#################################################################################

#Kill previous Teraterm sessions or continue
proc_tt_kill = "taskkill /IM ttermpro.exe /F"
logs_tt_move = "move /Y " + teralog + "*.log " + teraold

try:
    call(proc_tt_kill)
except FileNotFoundError:
    print("No Teraterm processes found to kill.")
finally:
    print("Continuing...") 

print(logs_tt_move)

try:
    call(logs_tt_move)
except FileNotFoundError:
    print("No log files found to move.")
finally:
    print("Continuing...") 

#################################################################################

#Get filename from -f command-line arguments
csvfile = open(filename)
reader=csv.DictReader(csvfile)
col_names = reader.fieldnames
#################################################################################

#Skip the entry if you set 1st row in csv config file to "no"
for row_count, row in enumerate(reader):
    if row[col_names[0]] == "no":
        no_run = "echo Entry " + row[col_names[5]] \
        + " slotted not to " + "run. Skipping..."
        print(no_run)
        continue
#################################################################################

#The parameters are different for each connection.  Decide which to use
#with the following if statements
#serial connection
    if row[col_names[0]] == "yes" and row[col_names[1]] == "serial":
        ser_entry = teramacro_ser + " " + "\"" + row[col_names[2]] + "\" " \
        + "\"" + row[col_names[3]] + "\" " + "\"" + row[col_names[4]] + "\" " \
        + "\"" + row[col_names[5]] + "\" " + "\"" + teralog + "\" "

#Turn print on to see how the commands are structured and issued.  Print can
#be turned off without issue
        print(ser_entry)
        call(ser_entry)
#Time delay goes here
        time.sleep(sec)
#################################################################################

#ssh connection
    if row[col_names[0]] == "yes" and row[col_names[1]] == "ssh":
        ssh_entry = teramacro_ssh + " " + "\"" + row[col_names[2]] + ":" \
            + row[col_names[3]] + "\" " + "\"" + row[col_names[4]] + "\" " \
            + "\"" + row[col_names[5]] + "\" " + "\"" + row[col_names[6]]  \
            + "\" " + "\"" + teralog + "\" "

        print(ssh_entry)
        call(ssh_entry)
        time.sleep(sec)
#################################################################################

#ports other than ssh
    if row[col_names[0]] == "yes" and row[col_names[1]] == "nossh":
        nossh_entry = teramacro_nossh + " " + "\"" + row[col_names[2]] + "\" " \
            + "\"" + row[col_names[3]] + "\" " + "\"" + row[col_names[4]] + "\" " \
            + "\"" + row[col_names[5]] + "\" " + "\"" + row[col_names[6]] + "\" " \
            + "\"" + teralog + "\" "

        print(nossh_entry)
        call(nossh_entry)
        time.sleep(sec)
#################################################################################

csvfile.close()