# Cobalt Strike Aggressor Scripts

## Introduction

This is a collection of Cobalt Strike Aggressor scripts I developed and tested while I was a Red Team member for Locked Shields 2021.

## Initial Access

[Initial Access](https://attack.mitre.org/tactics/TA0001/) consists of techniques that use various entry vectors to gain their initial foothold within a network. 

- `initial-access-cmd/initial-access-cmd.cna`:
    - **Certutil Web Delivery (Custom)**: Provides a CMD one-liner to deliver a custom executable via Certutil 
    - **Certutil Web Delivery (Stageless)**: Provides a CMD one-liner to deliver a stageless Cobalt Strike payload via Certutil 
    - **Bitsadmin Web Delivery (Stageless)**: Provides a CMD one-liner to deliver a stageless Cobalt Strike payload via Bitsadmin 
    - **Regsvr32 Web Delivery (Stageless)**: Provides a CMD one-liner to deliver a stageless Cobalt Strike payload via Regsvr32 
    - **MSHTA Web Delivery (Stageless)**: Provides a CMD one-liner to deliver a stageless Cobalt Strike payload via MSHTA 
    - **Rundll32 Web Delivery (Stageless)**: Provides a CMD one-liner to deliver a stageless Cobalt Strike payload via Rundll32 

- `initial-access-powershell/initial-access-powershell.cna`:
    - **Pure Powershell Web Delivery (Stageless)**: Provides a PowerShell one-liner to deliver (in-memory) a stageless Cobalt Strike PoweShell payload
    - **Artifact Powershell Web Delivery (Stageless)**: Provides a PowerShell one-liner to deliver (in-memory) a PowerShell scripts which embeds a stageless Cobalt Strike payload 

- `initial-access-python/initial-access-python.cna`:
    - **Python 2 Web Delivery**: Provides a Python 2 one-liner to deliver a stageless Cobalt Strike payload (it assumes the following path for Python 2: *c:\Python27\pythonw.exe*)
    - **Python 3 Web Delivery**: Provides a Python 3.9 one-liner to deliver a stageless Cobalt Strike payload (it assumes the following path for Python 3.9: *C:\Python39\pythonw.exe*)

## Persistence

[Persistence](https://attack.mitre.org/tactics/TA0003/) consists of techniques that adversaries use to keep access to systems across restarts, changed credentials, and other interruptions that could cut off their access.

- `persistence-sharpersist/persistence-sharpersist.cna`:
    - **\* Startup Folder (Upload executable) [Reboot]**: Installs persistence for all users by uploading an executable to the startup folder [Requires administrator privileges]
    - **Startup Folder (Upload executable) [Reboot]**: Installs persistence for the current user by uploading an executable to the startup folder
    - **\* Windows Service (Powershell command) [Reboot]**: Installs persistence for all users by creating a Windows service launching a PowerShell command [Requires administrator privileges]
    - **\* Windows Service (Upload executable) [Reboot]**: Installs persistence for all users by uploading an executable and creating a Windows service launching it [Requires administrator privileges]
    - **\* Scheduled Task (Powershell command) [Logon/Hourly]**: Installs persistence for all users by creating a Scheduled Task launching a PowerShell command [Requires administrator privileges]
    - **\* Scheduled Task (Upload executable) [Logon/Hourly]**: Installs persistence for all users by uploading an executable and creating a Scheduled Task launching it [Requires administrator privileges]
    - **Scheduled Task (Powershell command) [Logon/Hourly]**: Installs persistence for the current user by creating a Scheduled Task launching a PowerShell command
    - **Scheduled Task (Upload executable) [Logon/Hourly]**: Installs persistence for the current user by uploading an executable and creating a Scheduled Task launching it
    - **\* Registry (Powershell command) [Logon]**: Installs persistence for all users by adding a PowerShell command to an autorun registry key [Requires administrator privileges]
    - **\* Registry (Upload executable) [Logon]**: Installs persistence for all users by uploading an executable and adding it to an autorun registry key [Requires administrator privileges]
    - **Registry (Powershell command) [Logon]**: Installs persistence for the current user by adding a PowerShell command to an autorun registry key [Requires administrator privileges]
    - **Registry (Upload executable) [Logon]**: Installs persistence for the current user by uploading an executable and adding it to an autorun registry key
    - **\* Sticky Keys (CMD)**: Launches a CMD prompt in case of sticky keys or other accessibility tools (e.g., Narrator, Magnifier) execution 
    - **\* Sticky Keys (Beacon)**: Launches a Cobalt Strike beacon in case of sticky keys or other accessibility tools (e.g., Narrator, Magnifier) execution 

## Defense Evasion

[Defense Evasion](https://attack.mitre.org/tactics/TA0005/) consists of techniques that adversaries use to avoid detection throughout their compromise. Techniques used for defense evasion include uninstalling/disabling security software or obfuscating/encrypting data and scripts.

- `evasion-disable-defender/evasion-disable-defender.cna`:
    - **\* Disable AV/Firewall**: Disables Windows Defender [Requires administrator privileges]
    - **\* Add Exclusions (Auto)**: Automatically adds a list of paths and executables to the Windows Defender exclusions [Requires administrator privileges]
    - **\* Add Exclusions (Custom)**: Adds a custom path and executable to the Windows Defender exclusions [Requires administrator privileges]
    - **\* Add Exclusions (Extensions)**: Adds a custom file extension to the Windows Defender exclusions [Requires administrator privileges]
    - **\* Remove Definitions**: Removes Windows Defender definitions [Requires administrator privileges]
    
- `evasion-disable-edr/evasion-disable-edr.cna`
    - **\* Kill EDRs**: Tries to automatically kill all EDRs/AVs [Requires administrator privileges]
    - **\* Kill EDR (Custom)**: Tries to kill a custom EDR/AV [Requires administrator privileges]