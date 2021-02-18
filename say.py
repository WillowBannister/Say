import subprocess

lines = {}
count = 1
lines["q"] = "Quit"

with open("text.txt",'r') as f:
    for line in f:
        lines[count] = line[:-1]
        count = count + 1

while True:

    for line in lines:
        print(str(line) + " : " + lines[line])
    
    num = int(input())
    speak = "say '" + lines[num] + "'"
    subprocess.Popen(speak, shell=True)