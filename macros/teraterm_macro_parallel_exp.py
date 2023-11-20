import argparse, csv, sys, time
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

# Argument parsing and setup
parser = argparse.ArgumentParser(description='To set directory and source file')
parser.add_argument('-f', '--file', type=str, help='Teraterm sessions config file, Required', required=True)
parser.add_argument('-p', '--path', type=str, help='Teraterm sessions path to config file, Required', required=True)
parser.add_argument('-l', '--logpath', type=str, help='Teraterm sessions log file location, Required', required=True)
args = parser.parse_args()

filename = args.file
filepath = args.path
logpath = args.logpath

# Global variables
sec = 1
teralog = logpath + '\\'
teraold = teralog + 'old'
teramacro_ser = filepath + '\\ttpmacro.exe macros\\console.ttl'
teramacro_ssh = filepath + '\\ttpmacro.exe macros\\ssh.ttl'
teramacro_nossh = filepath + '\\ttpmacro.exe macros\\nossh.ttl'

# Function to launch a session
def launch_session(row):
    #print("Processing row:", row)
    if row['run'] == 'yes':
        command = ""
        if row['connection'] == 'serial':
            # Update the command construction with correct key names
            pass  # Replace with your command construction logic for serial connections
        elif row['connection'] == 'ssh':
            command = f"{teramacro_ssh} \"{row['target']}:{row['port']}\" \"{row['username']}\" \"{row['password']}\" \"{row['log_prefix']}\" \"{teralog}\" \"{row['window_title']}\""
        elif row['connection'] == 'nossh':
            # Update the command construction with correct key names
            pass  # Replace with your command construction logic for nossh connections

        print("Constructed command:", command)
        time.sleep(5)

        if command:
            try:
                subprocess.Popen(command, shell=True)
            except Exception as e:
                print(f"Error executing command: {e}")
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
        with ThreadPoolExecutor(max_workers=9) as executor:
            # Submitting tasks for each row in the CSV
            futures = [executor.submit(launch_session, row) for row in reader]

            # Wait for all tasks to complete and handle results
            for future in as_completed(futures):
                # Handle results, logging, or exceptions here
                pass

if __name__ == '__main__':
    main()
