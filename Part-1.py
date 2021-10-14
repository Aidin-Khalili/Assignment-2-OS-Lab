import math
exit = True
while exit:
    while True:
        choice = abs(int(input("Please enter your choice : \n 1. Calculate sinus \n 2. Calculate cosinus \n 3. Calculate tangent \n 4. Calculate cotangent\n 5. Calculate logaritm \n 6. Exit \n")))
        if choice>=1 and choice<=6 : 
            break
    match choice:
        case 1:
            num = float(input("Please enter your number :"))
            print(math.sin(math.radians(num)))
        case 2:
            num = float(input("Please enter your number :"))
            print(math.cos(math.radians(num)))
        case 3:
            num = float(input("Please enter your number :"))
            print(math.tan(math.radians(num)))
        case 4:
            num = float(input("Please enter your number :"))
            print(1/math.tan(math.radians(num)))
        case 5:
            num = abs(float(input("Please enter your number :")))
            print(math.log(num))
        case _:
            exit = False
print("Have good time ;)")