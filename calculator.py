print('enter operation')
operation = input()

if operation == "addition" or operation == "Addition" or operation == "+":
    print('enter number 1')
    num1 = input()
    print('enter number 2')
    num2 = input()
    addEq = int(num1)+int(num2)
    print("the answer to this addition question is "+str(addEq))
elif operation == "subtraction" or operation == "Subtraction" or operation == "-":
    print('enter number 1')
    num1 = input()
    print('enter number 2')
    num2 = input()
    addEq = int(num1)-int(num2)
    print("the answer to this subtraction question is "+str(addEq))
elif operation == "multiplication" or operation == "Multiplication" or operation == "*":
    print('enter number 1')
    num1 = input()
    print('enter number 2')
    num2 = input()
    addEq = int(num1)*int(num2)
    print("the answer to this multiplication question is "+str(addEq))
elif operation == "division" or operation == "Division" or operation == "/":
    print('enter number 1')
    num1 = input()
    print('enter number 2')
    num2 = input()
    addEq = int(num1)/int(num2)
    print("the answer to this division question is "+str(addEq))
else: 
    print("Non valid operation")

