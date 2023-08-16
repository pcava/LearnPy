Write-Output "---test email----"

Set-ExecutionPolicy Bypass -scope Process -Force # -Confirm:$false

try {

    & 'C:\ProgramData\Anaconda3\shell\condabin\conda-hook.ps1' ; conda activate 'C:\Users\CAVP\.conda\envs\paolo_efg'

    # cmd /c 'pause' # uncomment this line to debug

    & 'C:\Users\CAVP\.conda\envs\paolo_efg\python.exe' M:\Dev\Compliance\test_email.py

    # cmd /c 'pause' # uncomment this line to debug

}

catch{Write-Error "! error in M:\Dev\Compliance\test_email.py"}
