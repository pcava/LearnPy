@echo off

:: https://stackoverflow.com/questions/17063947/get-current-batchfile-directory
:: echo %cd% & :: path of the caller of the batch
:: echo %0 :: & :: name of the batch script itself e.g. scripts\mybatch.bat
:: echo %~dp0 & :: Drive and Path to the batch script (e.g. W:\scripts\)
:: echo %~f0 & :: full pathname (e.g. W:\scripts\mybatch.cmd
:: Move one level up to the root folder
cd %~dp0..

echo Script: %~f0 - Started on: %DATE:/=-% at: %TIME::=-% >> "scripts\LogEverything.txt"
echo. >> "scripts\LogEverything.txt"

:: Execute the test.bat script
:: call "scripts\test.bat"

:: Execute the test.bat script showing only the output
:: @call "scripts\test.bat"

:: Silence terminal output apart from potential errors
:: @call "scripts\test.bat" 1>NUL

:: Silence terminal output and send > potential errors to a log file
:: del "scripts\LogErrors.txt"
:: call "scripts\test.bat" 1>NUL 2>"scripts\LogErrors.txt"

:: https://stackoverflow.com/questions/503846/how-do-i-echo-and-send-console-output-to-a-file-in-a-bat-script
:: call "scripts\daily_task_1.bat" 1>> "scripts\LogOutput.txt" 2>> "scripts\LogErrors.txt"
:: call "scripts\daily_task_2.bat" > "scripts\LogEverything.txt" 2>&1

:: Execute the script and append >> both output and errors to a log file
del "scripts\LogEverything.txt"
call "scripts\caller_name.bat" >> "scripts\LogEverything.txt" 2>&1

@if NOT ["%errorlevel%"]==["0"] pause

echo Script: %~f0 - Ended on: %DATE:/=-% at: %TIME::=-% >> "scripts\LogEverything.txt"

exit
