@echo off

powershell -Command "gci D:\Logs\*.log | ? {$_.lastwritetime -lt (get-date).adddays(-7)} | compress-archive -DestinationPath D:\Logs\$(get-date -f yyyy-MM-dd)"
powershell -Command "gci D:\Logs\*.log | ? {$_.lastwritetime -lt (get-date).adddays(-7)} |  Remove-Item -Force

pause
