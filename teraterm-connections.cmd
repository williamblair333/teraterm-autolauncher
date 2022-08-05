rem python3 %cd%\teraterm_macro.py -f %cd%\teraterm_targets.csv -p %cd% -l %cd%\logs
rem python3 teraterm_macro.py -f teraterm_connections.csv -p C:\util\teraterm-4.106 -l C:\util\teraterm-4.106\logs

rem python3 C:\util\teraterm-4.106\macros\teraterm_macro.py -f C:\util\teraterm-4.106\macros\teraterm_targets.csv -p C:\util\teraterm-4.106 -l C:\util\teraterm-4.106\logs
python3 %cd%\macros\teraterm_macro.py -f %cd%\macros\teraterm_targets.csv -p %cd% -l %cd%\logs
pause