import subprocess
import time

def run_commands_in_background():
    # List of command line commands you want to run
    commands = ['glazewm', 'python autotiling.py']
    
    creationflags = subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS

    # Start each command in the background
    processes = []
    for cmd in commands:
        # Start the command and detach from it
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, creationflags=creationflags)
        processes.append(process)

time.sleep(5)
run_commands_in_background()