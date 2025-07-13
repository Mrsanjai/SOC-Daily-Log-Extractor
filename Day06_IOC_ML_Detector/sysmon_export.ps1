# sysmon_export.ps1
$logPath = "F:\SOC_Journey\GitHub_Pushes\Day06_IOC_ML_Detector\logs\sysmon_live.log"

while ($true) {
    Get-WinEvent -LogName "Microsoft-Windows-Sysmon/Operational" -MaxEvents 3 |
    ForEach-Object {
        $_.Message | Out-File -Append $logPath -Encoding utf8
        "powershell -EncodedCommand attack test" | Out-File -Append $logPath -Encoding utf8  # simulate
    }
    Start-Sleep -Seconds 5
}
