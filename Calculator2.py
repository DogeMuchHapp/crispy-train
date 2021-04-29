# Ur dumb ok, stop looking into other peoples junk, it's weird, pls stop
# Just download python, its a cool program, c# is dumb, don't run this in c# cause it'll act weird lol
# Imagine reading this in like notepad or something, kinda weird ngl
# Also just in case this makes it to CNN um, DMH!
num1 = float(input("Please input a number:"))
function = input("Please input a function (Add, Subtract, Multiply, Divide, Square, Cube):")
num2 = float(input("Please input a second number:"))
answer1 = input("Would you like to add a third number(yes/no)")
if answer1 == "yes":
    function2 = input("Please input a second function (Add, Subtract, Multiply, Divide, Square, Cube):")
    num3 = float(input("Please input a third number:"))
if function == "Add" and answer1 == "no":
    print(num1 + num2)
elif function == "Subtract" and answer1 == "no":
    print(num1 - num2)
elif function == "Multiply" and answer1 == "no":
    print(num1 * num2)
elif function == "Divide" and answer1 == "no":
    print(num1 / num2)
elif function == "Square" and answer1 == "no":
    print(num1 * num1)
elif function == "Cube" and answer1 == "no":
    print(num1 * num1 * num1)
elif function == "Add" and answer1 == "yes" and  function2 == "Add":
    print(num1 + num2 + num3)
elif function == "Subtract" and answer1 == "yes" and  function2 == "Add":
    print(num1 - num2 + num3)
elif function == "Multiply" and answer1 == "yes" and  function2 == "Add":
    print(num1 * num2 + num3)
elif function == "Divide" and answer1 == "yes" and  function2 == "Add":
    print(num1 / num2 + num3)
elif function == "Square" and answer1 == "yes" and  function2 == "Add":
    print(num1 * num1 + num3)
elif function == "Cube" and answer1 == "yes" and  function2 == "Add":
    print(num1 * num1 * num1 + num3)
elif function == "Add" and answer1 == "yes" and  function2 == "Subtract":
    print(num1 + num2 - num3)
elif function == "Subtract" and answer1 == "yes" and  function2 == "Subtract":
    print(num1 - num2 - num3)
elif function == "Multiply" and answer1 == "yes" and  function2 == "Subtract":
    print(num1 * num2 - num3)
elif function == "Divide" and answer1 == "yes" and  function2 == "Subtract":
    print(num1 / num2 - num3)
elif function == "Square" and answer1 == "yes" and  function2 == "Subtract":
    print(num1 * num1 - num3)
elif function == "Cube" and answer1 == "yes" and  function2 == "Subtract":
    print(num1 * num1 * num1 - num3)
elif function == "Add" and answer1 == "yes" and function2 == "Multiply":
    print(num1 + num2 * num3)
elif function == "Subtract" and answer1 == "yes" and function2 == "Multiply":
    print(num1 - num2 * num3)
elif function == "Multiply" and answer1 == "yes" and function2 == "Multiply":
    print(num1 * num2 * num3)
elif function == "Divide" and answer1 == "yes" and function2 == "Multiply":
    print(num1 / num2 * num3)
elif function == "Square" and answer1 == "yes" and function2 == "Multiply":
    print(num1 * num1 * num3)
elif function == "Cube" and answer1 == "yes" and function2 == "Multiply":
    print(num1 * num1 * num1 * num3)
elif function == "Add" and answer1 == "yes" and function2 == "Divide":
    print(num1 + num2 / num3)
elif function == "Subtract" and answer1 == "yes" and function2 == "Divide":
    print(num1 - num2 / num3)
elif function == "Multiply" and answer1 == "yes" and function2 == "Divide":
    print(num1 * num2 / num3)
elif function == "Divide" and answer1 == "yes" and function2 == "Divide":
    print(num1 / num2 / num3)
elif function == "Square" and answer1 == "yes" and function2 == "Divide":
    print(num1 * num1 / num3)
elif function == "Cube" and answer1 == "yes" and function2 == "Divide":
    print(num1 * num1 * num1 / num3)
elif function == "Add" and answer1 == "yes" and function2 == "Square":
    print(num1 + num3 * num3)
elif function == "Subtract" and answer1 == "yes" and function2 == "Square":
    print(num1 - num3 * num3)
elif function == "Multiply" and answer1 == "yes" and function2 == "Square":
    print(num1 * num3 * num3)
elif function == "Divide" and answer1 == "yes" and function2 == "Square":
    print(num1 / num3 * num3)
elif function == "Square" and answer1 == "yes" and function2 == "Square":
    print(num1 * num1 + num3 * num3)
elif function == "Cube" and answer1 == "yes" and function2 == "Square":
    print(num1 * num1 * num1 + num3 * num3)
elif function == "Add" and answer1 == "yes" and function2 == "Cube":
    print(num1 + num3 * num3 * num3)
elif function == "Subtract" and answer1 == "yes" and function2 == "Cube":
    print(num1 - num3 * num3 * num3)
elif function == "Multiply" and answer1 == "yes" and function2 == "Cube":
    print(num1 * num3 * num3 * num3)
elif function == "Divide" and answer1 == "yes" and function2 == "Cube":
    print(num1 / num3 * num3 * num3)
elif function == "Square" and answer1 == "yes" and function2 == "Cube":
    print(num1 * num1 + num3 * num3 * num3)
elif function == "Cube" and answer1 == "yes" and function2 == "Cube":
    print(num1 * num1 * num1 + num3 * num3 * num3)
continue1 = input("Are you satisfied?")
print("You just got pranked!")
