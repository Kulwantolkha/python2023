user_info= "kulwant olkha is a 19 year old boy".split( )
print(user_info)
user= "Sanchit,is,a,15,year,old,boy".split(",")
print(user)
name,age=input("enter your name and age : ").split(",")
print(name)
print(age)
new_user=["Prakash","45"]
print(",".join(new_user))

def greater(a,b,c):
    if a>b:
        return ("a is greater than b")
    elif a>c:
        return ("a is greater than c")
    elif b>a:
        return ("b is greater than a")
    elif b>c:
        return ("b is greater than c")
    elif c>a:
        return ("c ia greater than a")
    elif c>b:
        reutrn ("c is greater than b")
    if a>b>c:
        return ("a is greater than b and c")
    elif b>a>c:
        return ("b is greater than a and c")
    elif c>a>b:
        return ("c is greater than a and b")

a= int(input("enter a number: "))
b=int(input("enter another number: "))
c=int(input("enter another number: "))
print(greater(a, b, c))


def is_palindrome(a):
    if a == a[::-1]:
        return True
    else: 
        return False

a = input("Enter a number : ")
print(is_palindrome(a))


