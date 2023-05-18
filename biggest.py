def big(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2
def large(num1,num2,num3):
    return big(big(num1,num2),num3)
for i in range(3):
    num1 = int(input('Enter your first number: '))
    num2 = int(input('Enter your second number: '))
    num3 = int(input('Enter your third number: '))
    print(large(num1,num2,num3))
exit()