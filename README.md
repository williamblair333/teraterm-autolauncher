# TeraTerm AutoLauncher

This tool contains 3 custom ttl files used to launch serial, ssh, and custom ipv4 
ports automatically. The user need only install the prerequisite software and 
populate the csv file with the desired connection information. An example 
file is included.

## Prerequisites
- Windows 10 22H2
- Python 3.6+
- Teraterm 4.1.06

### Python Installation
- Use admin privileges when installing py.exe.
- Add python.exe to PATH.
- Customize installation:
  - Check all optional boxes.
  - Check all advanced options except symbols and debug binaries.
- Install to `C:\util\python\Python312`.
- Click Disable path length limit.
- Update the path statement with `C:\util\python\Python312` if necessary (should be automatic).

### Teraterm Installation
- Custom Installation. **Install to a folder you have write permissions for, such as `C:\util\teraterm`.**
- Accept other defaults.
- Place a Desktop shortcut and ensure it's pointing to the correct folder.

### Additional Setup
- **GitHub**: Clone the repo locally. The goal is to copy logs, macros, and `teraterm-connections.cmd` into `c:\util\teraterm`.
- **Windows**: Create a shortcut of `teraterm-connections.cmd` and place it on the desktop.
- **Test Machine**: Transfer `wait_for_esc.sh` to a test Linux server and set permissions with `chmod +x`.
- Log out of your Windows session and log back in.

## Download locations
- [Python](https://www.python.org/downloads/)
- [Teraterm](https://osdn.net/projects/ttssh2/releases/)

**Note:**  
All .ttl, .csv, and .py files should go into the Teraterm macros directory. Will it work elsewhere? Maybe. It wasn't tested elsewhere though.

## Usage Example

teraterm_macro.py -f teraterm_targets.csv -p C:\util\teraterm-4.106 -l C:\util\teraterm-4.106\logs

csharp


The complete invocation syntax is:

teraterm_macro.py -f csv name -p teraterm app root folder -l log file location

markdown


The CSV consists of 7 columns:  
- run
- connection
- target
- port
- username
- password
- log_prefix

### Descriptions of each column:
- **run**: If set to 'no', the script ignores the connection information.
- **connection**: Must use either 'serial', 'ssh', or 'nossh'.
- **username**: Leave blank if there is no username.
- **password**: Leave blank if there is no password.
- **log_prefix**: This will prepend the log file name (which is date-stamped automatically).

**Note**: Serial/COM port connections only need 6 entries, see the examples. This will be fixed for completeness later.  
The first line of the CSV file is ignored.

## CSV Examples (Now you can set the baud rate!)

-<csv>-
run,connection,target,port,username,password,log_prefix
yes,serial,19,115200,,Cisco-COM19-
yes,ssh,192.168.1.2,22,root,penguinzrule,server2-
no,nossh,192.168.1.25,23,admin,telnetrockz,server3-
yes,nossh,192.168.1.25,23,admin,telnetrockz,server3-
</csv>-
