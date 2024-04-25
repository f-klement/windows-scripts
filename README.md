# windows-scripts
under duress I found ways of replicating my hyprland setup solely within the windows user space

requirements:
- git bash
- choco & scoop
- glazeWM
- python 3.11+ (platform, asyncio, websockets, subprocess)
- powertoys
- windhawk (taskbarheight)
- snipaste
- VS Code
- brave
- Windows Terminal
- mingwe/mysy2
- obsidian

The repo provides merely the config for glazeWM, as well as an autotiling and autostart script for the two. 
Windhawk and powertoys need to be started seperately, either through task scheduler or optionally inclusion 
in the autostart script. Powertoys Run requires the centralized keyboard hook setting to be turned on.
