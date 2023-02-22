Write-Host "X
X:
X:
X:
X:
X:
X:
" -ForegroundColor Green
Write-Host "
********************************************
***Choose one of the X's from the list***
********************************************" -ForegroundColor Red

$xml 		= [xml](Get-Content C:\Temp\file.config)
$node_value = $xml.SelectNodes("//SomeNodeFromTheXML")[0].getAttribute("SomeAttributeOfTheNode")
Write-Host "Current X:"$node_value -ForegroundColor Green
Write-Host "Set new X "-ForegroundColor Green

$newValue = Read-Host
$node 		= $xml.SelectNodes("//SomeNodeFromTheXML")[0].SetAttribute("name", $newValue)
Write-Host "New X: "$newValue -ForegroundColor Red
$xml.Save("C:\Temp\file.config")

#Start-Process -FilePath "C:\Program Files (x86)\Some.exe"
