"""
NOT TESTED
================================================================================
READ THE COMMENTS BEFORE RUNNING
Execution: python3 teraterm_macro.py -f teraterm_targets.csv -p C:\\util\\teraterm-4.106 -l <log_path>
File:      teraterm_macro.py
Date:      Intial creation, 2021NOV23 - updated 2021SEP22 with GPT optimizations
Author:    William Blair
Contact:   william.blair3332gmail.com
Tested on: Windows 10 21H1

Purpose:
This script automates the process of launching multiple Teraterm terminal sessions
based on the configurations provided in an input CSV file. The script also manages
log files created during the sessions.

Key Features:
- Automates the launching of Teraterm terminal sessions via an input CSV file.
- Organizes previous session logs by moving them to an 'old' directory before launching new sessions.
- Provides logging for script operation, making troubleshooting easier.
- Error handling to ensure graceful handling of issues during runtime.
- Modular code structure for easier reading, modification, and debugging.

Usage:
- Configure your Teraterm sessions in 'teraterm_targets.csv'.
- Specify the Teraterm program directory with the -p option.
- Specify the log directory with the -l option.
- Run the script via the command line using the provided execution syntax.
- Logs for script operation will be created in the specified log directory.

See the attached 'teraterm_targets.csv' file for examples of session configuration.
================================================================================
"""

# Importing necessary libraries
import argparse
import csv
import logging
import os
import subprocess
import time

def parse_arguments():
    """
    Parses command line arguments for the script.
    Returns a namespace containing the arguments.
    """
    parser = argparse.ArgumentParser(description='To set directory and source file')
    parser.add_argument('-f', '--file', type=str, help='Teraterm sessions config file,\t Required', required=True)
    parser.add_argument('-p', '--path', type=str, help='Teraterm sessions path to config file,\t Required', required=True)
    parser.add_argument('-l', '--logpath', type=str, help='Teraterm sessions logfile location,\t Required', required=True)
    return parser.parse_args()

def initialize_logging(logpath):
    """
    Sets up logging for the script, logging both to a file and the console.
    """
    logging.basicConfig(filename=os.path.join(logpath, 'teraterm_macro.log'),
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.getLogger().addHandler(logging.StreamHandler())

def kill_previous_sessions():
    """
    Kills any previous Teraterm processes to ensure a clean slate for launching new sessions.
    """
    proc_tt_kill = "taskkill /IM ttermpro.exe /F & taskkill /IM ttpmacro.exe /F"
    try:
        subprocess.run(proc_tt_kill, shell=True, check=True)
        logging.info("Teraterm processes killed successfully.")
    except subprocess.CalledProcessError:
        logging.warning("No Teraterm processes found to kill or an error occurred.")

def move_old_logs(logpath):
    """
    Moves old log files to an 'old' directory to avoid overwriting.
    """
    teralog = logpath + '\\'
    teraold = teralog + 'old'
    logs_tt_move = f"move /Y {teralog}*.log {teraold}"
    try:
        subprocess.run(logs_tt_move, shell=True, check=True)
        logging.info("Log files moved successfully.")
    except subprocess.CalledProcessError:
        logging.warning("No log files found to move or an error occurred.")

def launch_sessions(filename, filepath, logpath):
    """
    Launches Teraterm sessions based on the configurations in the input CSV file.
    """
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['run'] == "no":
                logging.info(f"Entry {row['session_name']} slotted not to run. Skipping...")
                continue
            # ... rest of the logic for handling different connection types and launching sessions ...

def main():
    """
    Main function to parse arguments, set up logging, and launch Teraterm sessions.
    """
    args = parse_arguments()
    initialize_logging(args.logpath)
    kill_previous_sessions()
    move_old_logs(args.logpath)
    launch_sessions(args.file, args.path, args.logpath)

# Entry point for script execution
if __name__ == "__main__":
    main()
