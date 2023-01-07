total = 0
i=0
while i<=10:
    total =total+i
    i=i+1
    print(total)
    print(i)

total=0
a=0
x=int(input("Enter a Number: "))
while a<=x:
    total= total +a
    a=a+1
    
print(total)

b= input()
print(int(b[0])+int(b[1])+int(b[2]))

k=input("Enter a number: ")
total=0
p=0
while p < len(k):
    total = total + int(k[p])
    p=p+1
print(total)


name=input("Please Enter Your Name : ")
temp=""
i=0
total=0
while i< len(name):
    if name[i] not in temp:
        temp = temp + name[i]
        print(f"{name[i]} : {name.count(name[i])}")
        i =i+1
