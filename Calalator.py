# Ur dumb ok, stop looking into other peoples junk, it's weird, pls stop
# Just download python, its a cool program, c# is dumb, don't run this in c# cause it'll act weird lol
# Imagine reading this in like notepad or something, kinda weird ngl
# Also just in case this makes it to CNN um, DMH!
answer1 = 0
num1_1 = 0
func_1 = "0"
num1_2 = 0
func_2 = "0"
num2_2 = 0
num1_3 = 0
func_3 = "0"
num2_3 = 0
func2_3 = "0"
num3_3 = 0
while answer1 != "1" or "2" or "3":
    answer1 = input("How many numbers would you like to use in this equation?(1-3):")

    if answer1 == "1":
        num1_1 = float(input("What is your first number?:"))
        func_1 = input("What is your (first) function?(+,-,*,/,Square,Cube):")
    if answer1 == "2":
        num1_2 = float(input("What is your first number?:"))
        func_2 = input("What is your (first) function?(+,-,*,/,Square,Cube):")
        num2_2 = float(input("What is your second number?:"))
    if answer1 == "3":
        num1_3 = float(input("What is your first number?:"))
        func_3 = input("What is your (first) function?(+,-,*,/,Square,Cube):")
        num2_3 = float(input("What is your second number?:"))
        func2_3 = input("What is your second function?(+,-,*,/,Square,Cube):")
        num3_3 = float(input("What is your third number:"))

if func_1 == "Square" and answer1 == "1":
    print(num1_1 * num1_1)
elif func_1 == "Cube" and answer1 == "1":
    print(num1_1 * num1_1 * num1_1)
elif func_2 == "+" and answer1 == "2":
    print(num1_2 + num2_2)
elif func_2 == "-" and answer1 == "2":
    print(num1_2 - num2_2)
elif func_2 == "*" and answer1 == "2":
    print(num1_2 * num2_2)
elif func_2 == "/" and answer1 == "2":
    print(num1_2 / num2_2)
elif func_3 == "+" and answer1 == "3" and func2_3 == "+":
    print(num1_3 + num2_3 + num3_3)
elif func_3 == "-" and answer1 == "3" and func2_3 == "+":
    print(num1_3 - num2_3 + num3_3)
elif func_3 == "*" and answer1 == "3" and func2_3 == "+":
    print(num1_3 * num2_3 + num3_3)
elif func_3 == "/" and answer1 == "3" and func2_3 == "+":
    print(num1_3 / num2_3 + num3_3)
elif func_3 == "+" and answer1 == "3" and func2_3 == "-":
    print(num1_3 + num2_3 - num3_3)
elif func_3 == "-" and answer1 == "3" and func2_3 == "-":
    print(num1_3 - num2_3 - num3_3)
elif func_3 == "*" and answer1 == "3" and func2_3 == "-":
    print(num1_3 * num2_3 - num3_3)
elif func_3 == "/" and answer1 == "3" and func2_3 == "-":
    print(num1_3 / num2_3 - num3_3)
elif func_3 == "+" and answer1 == "3" and func2_3 == "*":
    print(num1_3 + num2_3 * num3_3)
elif func_3 == "-" and answer1 == "3" and func2_3 == "*":
    print(num1_3 - num2_3 * num3_3)
elif func_3 == "*" and answer1 == "3" and func2_3 == "*":
    print(num1_3 * num2_3 * num3_3)
elif func_3 == "/" and answer1 == "3" and func2_3 == "*":
    print(num1_3 / num2_3 * num3_3)
elif func_3 == "+" and answer1 == "3" and func2_3 == "/":
    print(num1_3 + num2_3 / num3_3)
elif func_3 == "-" and answer1 == "3" and func2_3 == "/":
    print(num1_3 - num2_3 / num3_3)
elif func_3 == "*" and answer1 == "3" and func2_3 == "/":
    print(num1_3 * num2_3 / num3_3)
elif func_3 == "/" and answer1 == "3" and func2_3 == "/":
    print(num1_3 / num2_3 / num3_3)
input("Please provide feedback:")
print("You just got pranked, your opinion doesn't matter, HA!")
