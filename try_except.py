# try:
#     a = int(input("Enter number: "))
#     print(a)
# except:
#     print("Some Error Occurred")

try:
    a = int(input("a: "))
    b = int(input("b: "))

    c = a + b
    d = a / b
    e = a * b

    if a == 0:
        f = fun1(a)
    print("try successful")
except ZeroDivisionError:
    print("zero division error occurred")
except NameError:
    print("name error occurred")
except Exception:
    print("exception occurred")


def fun1(n):
    print(n)


try:
    a = int(input("a: "))
    b = int(input("b: "))

    c = a+b
    d = a/b
    e = a*b
    if a == 0:
        f = fun1(a)
    print("try successful")
except ZeroDivisionError:
    print("zero division occurred")
except ArithmeticError:
    print("arithmetic error occurred")
except Exception:
    print('exception occurred')

def fun1(m):
    print(m)


