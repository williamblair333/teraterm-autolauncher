
import argparse, csv, sys, time
import os
from subprocess import call
from concurrent.futures import ThreadPoolExecutor

# Argument parsing and setup
parser = argparse.ArgumentParser(description='To set directory and source file')
parser.add_argument('-f', '--file', type=str, help='Teraterm sessions config file,\t Required', required=True)
parser.add_argument('-p', '--path', type=str, help='Teraterm sessions path to config file,\t Required', required=True)
parser.add_argument('-l', '--logpath', type=str, help='Teraterm sessions log file location,\t Required', required=True)
args = parser.parse_args()

filename = args.file
filepath = args.path
logpath  = args.logpath

# Global variables
sec = 1
teralog = logpath + '\\'
teraold = teralog + 'old'
teramacro_ser = filepath + '\\ttpmacro.exe macros\\console.ttl'
teramacro_ssh = filepath + '\\ttpmacro.exe macros\\ssh.ttl'
teramacro_nossh = filepath + '\\ttpmacro.exe macros\\nossh.ttl'

# Function to launch a session
def launch_session(row):
    if row['Run'] == 'yes':
        if row['Type'] == 'serial':
            ser_entry = f"{teramacro_ser} "{row['Port']}" "" "" "{row['Name']}" "{teralog}" "{row['LogName']}" "
            print(ser_entry)
            call(ser_entry)
        elif row['Type'] == 'ssh':
            ssh_entry = f"{teramacro_ssh} "{row['IP']}:{row['Port']}" "{row['Username']}" "{row['Password']}" "{row['Name']}" "{teralog}" "{row['LogName']}" "
            print(ssh_entry)
            call(ssh_entry)
        elif row['Type'] == 'nossh':
            nossh_entry = f"{teramacro_nossh} "{row['IP']}" "{row['Port']}" "{row['Username']}" "{row['Password']}" "{row['Name']}" "{teralog}" "{row['LogName']}" "
            print(nossh_entry)
            call(nossh_entry)
        time.sleep(sec)

# Main script logic
def main():
    # Kill previous Teraterm sessions
    proc_tt_kill = "taskkill /IM ttermpro.exe /F & taskkill /IM ttpmacro.exe /F"
    try:
        os.system(proc_tt_kill)
    except FileNotFoundError:
        print("No Teraterm processes found to kill.")
    finally:
        print("Continuing...") 

    # Move old logs
    logs_tt_move = f"move /Y {teralog}*.log {teraold}"
    try:
        os.system(logs_tt_move)
    except FileNotFoundError:
        print("No log files found to move.")
    finally:
        print("Continuing...") 
    print(logs_tt_move)

    # Reading CSV file and launching sessions in parallel
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        with ThreadPoolExecutor(max_workers=16) as executor:
            futures = [executor.submit(launch_session, row) for row in reader]
            for future in concurrent.futures.as_completed(futures):
                pass  # Handle results, logging, or exceptions here

if __name__ == '__main__':
    main()
