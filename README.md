# windows-scripts
Under duress I found ways of replicating my hyprland setup solely within the windows user space.
I despise powershell and am much more comfortable in bash, but some concessions had to be made.
Given that glazeWM is an i3 and polybar port, autotiling is not a goal of the project and 
needed to be manually simulated. The polybar port does not fully make use of all windows apis, 
so some of the widgets do not provide full functionality.

requirements:
- git bash: https://gitforwindows.org/
- choco & scoop: https://chocolatey.org/  &  https://scoop.sh/
- glazeWM: https://github.com/glzr-io/glazewm (in the V3 incompatible with the burgr033 script, refer to ParasiteDelta instead)
- python 3.11+ (platform, asyncio, websockets, subprocess)
- https://github.com/ParasiteDelta/GAT-GWM (dynamic tiling script built in rust)
- powertoys
- windhawk (taskbarheight): https://windhawk.net/
- snipaste
- VS Code
- chrome(ium)/brave
- Windows Terminal
- mingwe/mysy2: https://www.mingw-w64.org/
- obsidian

The repo provides merely the config for glazeWM, as well as an autotiling and autostart script for the two,
building upon the autotiling implementation by burgr033, the Rust based variant by ParasiteDelta fulfills the same function.
Windhawk and powertoys need to be started seperately, either through task scheduler or optionally inclusion in the autostart script. 
The new V3 glazr folder needs a dot '.' added to its title to be found and run correctly.
Powertoys Run requires the centralized keyboard hook setting to be turned on.
