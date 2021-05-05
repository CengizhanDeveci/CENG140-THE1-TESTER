import random as random

count = 0
while count < 1000:
    file = open(f"inputs/input{count}.txt","w")
    for i in range(0,25):
        for j in range(0,24):
            file.write(f"{random.randint(0,7)} ")   
        file.write(f"{random.randint(0,7)}\n")
    file.write("F\n")
    file.write(f"{random.randint(-50,50)} {random.randint(-50,50)}\n")
    file.write(f"{random.randint(0,24)} {random.randint(0,24)}")

    file.close()
    count += 1

while count <1500:
    file = open(f"inputs/input{count}.txt","w")
    for i in range(0,25):
        for j in range(0,24):
            file.write(f"{random.randint(0,7)} ")   
        file.write(f"{random.randint(0,7)}\n")
    file.write("P\n")
    

    width = random.randint(0,12)
    length = random.randint(0,12)
    x = random.randint(width+1,24)
    x1 = random.randint(0,x)
    y = random.randint(length+1,24)
    y1 = random.randint(0,y)
    while (x < 0 or x >= 25 or x1 < 0 or x1 >= 25 or y1 < 0 or y1 >= 25 or y < 0 or y >= 25 or x+width < 0 or x+width >= 25 or x-width < 0 
    or x-width >= 25 or y1-length < 0 or y1-length >= 25 or y+length < 0 or y+length >= 25  or x1+width < 0 or x1+width >= 25 or x1-width < 0 
    or x1-width >= 25):
        width = random.randint(0,12)
        length = random.randint(0,12)
        x = random.randint(width+1,24)
        x1 = random.randint(0,x-1)
        y = random.randint(length+1,24)
        y1 = random.randint(0,y-1)

    if random.randint(0,1):
        if random.randint(0,1):
            file.write(f"{x} {y} {x+width} {y+length}\n")
            file.write(f"{x1} {y1} {x1-width} {y1-length}\n")
        else:
            file.write(f"{x+width} {y+length} {x} {y}\n")
            file.write(f"{x1-width} {y1} {x1} {y1-length}\n")
    else:
        if random.randint(0,1):
            file.write(f"{x1} {y1} {x1-width} {y1-length}\n")
            file.write(f"{x} {y} {x+width} {y+length}\n")
        else:
            file.write(f"{x+width} {y+length} {x} {y}\n")
            file.write(f"{x1-width} {y1} {x1} {y1-length}\n")

    count += 1

while count <2500:
    file = open(f"inputs/input{count}.txt","w")
    for i in range(0,25):
        for j in range(0,24):
            file.write(f"{random.randint(0,7)} ")   
        file.write(f"{random.randint(0,7)}\n")
    file.write("R\n")
    rotate = random.choice([0,90,180,270])
    if random.randint(0,1):
        file.write(f"R {rotate}\n")
    else:
        file.write(f"L {rotate}\n")
        
    a = random.randint(0,12)
    x = random.randint(0,24-a)
    x1 = random.randint(0,24-a)

    y = random.randint(0,24-a)
    y1 = random.randint(0,24-a)

    
    while not (x + a < 25 and x1 + a < 25 and y + a < 25 and y1 + a < 25 and ((x + a < x1 or x1 + a < x) or (y+a<y1 or y1+a<y)) ):
        a = random.randint(0,12)
        x = random.randint(0,24-a)
        x1 = random.randint(0,24-a)

        y = random.randint(0,24-a)
        y1 = random.randint(0,24-a)
    else:
        file.write(f"{x} {y} {x+a} {y+a}\n")
        file.write(f"{x1} {y1} {x1+a} {y1+a}\n")

    count += 1
    