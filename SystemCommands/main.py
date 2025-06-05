import subprocess
subprocess.run(["ls", "-l"])
subprocess.run(["ls", "-l", "/mnt/c/cprogramming"]) # passing a directory where command 
# should be executed

result = subprocess.run(["whoami"], capture_output=True, text=True)
print("Current user:", result.stdout.strip())  # strip is used to remove any leading or trailing whitespaces including newline character



"""
Example: 
1. Run Python script in another folder

subprocess.run(["python3", "script.py"], cwd="/home/lakshit/projects/")

2. Run a command and handle error

try:
    subprocess.run(["ls", "/invalid/path"], check=True)
except subprocess.CalledProcessError:
    print("Command failed")

""" 