import subprocess
import platform

count = 0
while count < 2500:
    myinput = open(f'inputs/input{count}.txt')
    myoutput = open(f'myoutputs/output{count}.txt', 'w')
    if platform.system() == "Windows":
        p = subprocess.Popen('the1.exe', stdin=myinput, stdout=myoutput)
    else:
        p = subprocess.Popen('./the1', stdin=myinput, stdout=myoutput)
    p.wait()
    myoutput.flush()
    count += 1

true = 0
wrong = 0

count = 0
while count < 2500:
    f1 = open(f"myoutputs/output{count}.txt")
    f2 = open(f"outputs/output{count}.txt")

    
    result = (f1.read() == f2.read())
    if result == True:
        true += 1
    else:
        wrong += 1
        print(count)

    count += 1

print(f"Wrong: {wrong}")
print(f"true: {true}")

print(f"Average: {true/(wrong+true)*100}%")
