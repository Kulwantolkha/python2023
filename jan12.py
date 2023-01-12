fruits=("mango","apple","kiwi")
fruit1,fruit2,fruits3=(fruits)
print(fruit2)

fruits1=("mango",["apple","kiwi"],1,3,4,[5,6,78])
fruits2=(1,3,4,5,6,78)
fruits1[1].pop()
fruits1[1].append("banana")
print(fruits)
print(min(fruits))
print(max(fruits))

 #funciton returning two values
def func(int1,int2):
     add = int1 + int2
     multiply = int1*int2
     return add,multiply
     print(func(2, 3))
add, multiply = func(3, 6)
print(add)
print(multiply)

num = tuple(range(1,11))
print(num)
print(str(num))

user = {"Name":"Kulwant","Age":"19","Language":"Python"}
print(type(user))
print(user)
user1=dict(Name="Sanchit",Age="14",Language="Java")
print(type(user1))
print(user1)
print(user["Name"])
print(user1["Age"])
user2 = {
     "Name" : "XYZ",
     "Age" : "X",
     "Fav_Movies" : ["yz",'xy','zx']
 }
print(user2)

user3 = {}
user3["name"]="Mohit"
user3["age"]="24"
print(user3)
for i in user:
    print(i)
for i in user:
    print(user[i])
print(user.values())
print(user.keys())
if "19" in user.values():
    print("Yes")
else:
    print("No")
print(user.items())

for key,values in user.items():
    print(f"key is {key} and value of this key is {values}")

user["college"]="LPU"
print(user)

user4 = user.pop("college")
print(user)
print(f"popped item is {user4}")
#random removal of items from dict
user5= user.popitem()
print(user)
print(f"randomly removed popped item is {user5}")
more= {"State": "Rajasthan","Current City":"Jalandhar"}
user.update(more)
print((user))
#from keys
d= dict.fromkeys(("name","age","height"), "unknown")
print(d)
e=dict.fromkeys("abc","unknown")
print(e)
f= dict.fromkeys(["name","age"],["unknown","unknown"])
print(f)
print(f["name"])
print(d.get("name"))
d.clear()
print(d)
d1=d.clear()
print(d1)
print(user.get("state","not found"))
