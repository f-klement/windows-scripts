# windows-scripts
under duress I found ways of replicating my hyprland setup solely within the windows user space

requirements:
- git bash: https://gitforwindows.org/
- choco & scoop: https://chocolatey.org/  &  https://scoop.sh/
- glazeWM: https://github.com/glzr-io/glazewm
- python 3.11+ (platform, asyncio, websockets, subprocess)
- powertoys
- windhawk (taskbarheight): https://windhawk.net/
- snipaste
- VS Code
- chrome(ium)/brave
- Windows Terminal
- mingwe/mysy2: https://www.mingw-w64.org/
- obsidian

The repo provides merely the config for glazeWM, as well as an autotiling and autostart script for the two,
building upon the autotiling implementation by burgr033. Windhawk and powertoys need to be started seperately,
either through task scheduler or optionally inclusion in the autostart script. 
Powertoys Run requires the centralized keyboard hook setting to be turned on.
