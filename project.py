#!/usr/bin/python

import cgi
import subprocess

print("Content-Type: text/plain;charset=utf-8")
print()

storage = cgi.FieldStorage()
command = storage.getvalue("x")

if command is None:
    output = "No output"

elif "date" in command or "Date" in command or "DATE" in command:
    output = subprocess.getoutput("date")

elif "memory" in command or "mem" in command or "Memory" in command:
    output = subprocess.getoutput("free -m")

elif "disk" in command or "space" in command or "Disc" in command or "Disk" in command:
    output = subprocess.getoutput("df -h")

elif "ip" in command or "IP" in command:
    output = subprocess.getoutput("ifconfig")

elif "cal" in command or "calender" in command or "Cal" in command or "Calender" in command:
    output = subprocess.getoutput("cal")

elif "files" in command or "file" in command:
    output = subprocess.getoutput("ls -a")

elif "images" in command or "image" in command or "img" in command:
    output = subprocess.getoutput("docker images")

elif "pull" in command and ("image" in command or "img" in command) and "ubuntu" in command:
    output = subprocess.getoutput("docker pull ubuntu")

elif "pull" in command and ("image" in command or "img" in command) and "nginx" in command:
    output = subprocess.getoutput("docker pull nginx")

elif "version" in command:
    output = subprocess.getoutput("docker -v")

elif "run" in command or "launch" in command and "ubuntu" in command:
    output = subprocess.getoutput("docker run -d ubuntu")

elif "run" in command or "launch" in command and "nginx" in command:
    output = subprocess.getoutput("docker run -d nginx")

elif "container" in command and "list" in command:
    output = subprocess.getoutput("docker ps -a") 

else:
    output = "Invalid command. Try another."

print(output)
