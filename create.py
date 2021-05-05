import subprocess
import platform

count = 0
while count < 2500:
    myinput = open(f'inputs/input{count}.txt')
    myoutput = open(f'outputs/output{count}.txt', 'w')
    if platform.system() == "Windows":
        p = subprocess.Popen('the1.exe', stdin=myinput, stdout=myoutput)
    else:
        p = subprocess.Popen('./the1', stdin=myinput, stdout=myoutput)
    p.wait()
    myoutput.flush()
    count += 1
