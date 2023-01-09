def add(a,b):
    return a+b
a= int(input("enter a number: "))
b= int(input("enter anotner number: "))
print(add(a, b))

c = input("enter first name : ")
d = input("enter second name : ")
print(add(c, d))

#return vs print
def add_three(a,b,c):
    print(a+b+c)

e= input("enter a number : ")
f= input("enter second number: ")
g= input("enter third number: ")
add_three(e, f, g)

def last(a):
    return a[len(a)-1]

a=input("enter a word: ")
print(last(a))

def is_even(num):
    if num%2==0:
        return True
    return False
num= int(input("Enter a number: "))
print(is_even(num))

def fibonacci_seq(n):
    a = 0 
    b = 1
    if n==1:
        print(a)
    elif n ==2:
        print(a,b)
    else:
        print(a,b, end=" ")
        for i in range(n-2):
            c = a + b
            a = b
            b=c
            print(b, end =" ")

n=45
print(fibonacci_seq(n))
