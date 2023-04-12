@echo off
:: Prevent echoing all commands in a batch file, include the echo off command at the beginning of the file
:: Prevents the prompt and contents of the batch file from being displayed, so that only the output is visible
:: Prevent echoing a particular command in a batch file, insert an @ sign in front of the command.
 
:: REM print "Hello World"
:: echo "Hello world"

:: REM print the path and file name
:: echo %~f0

:: REM print the date
:: echo Date: %DATE:/=-% and Time: %TIME::=-%

:: REM will print the comment in the terminal
:: will NOT print the comment in the terminal

echo Script: %~f0
echo Date: %DATE:/=-% and Time:%TIME::=-%

:: Move one level up to the root folder
cd %~dp0..

:: Execute a python script with specific env
:: call "C:\ProgramData\Anaconda3\Scripts\activate.bat" "C:\Users\CAVP\.conda\envs\paolo_env"
:: "C:\Users\CAVP\.conda\envs\paolo_efg\python.exe" "test_email.py"
:: pause :: uncomment this line to debug

:: https://coderwall.com/p/jexjlw/pause-on-error-in-batch-file
if NOT ["%errorlevel%"]==["0"] pause