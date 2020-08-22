# Definition
def CGCD(a,b):
    if b==0:
        return a
    else:
        return CGCD(b,a%b)
Check = False
# Input value
try:
    num1 = int(input("enter the first number:"))
    num2 = int(input("enter the second number:"))
# Output result
    print(CGCD(num1,num2))
    Check = True
except:
    print("Invalid input, please try again!")
