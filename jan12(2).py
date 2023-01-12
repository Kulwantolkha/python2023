def cubic(c):
    cube={}
    for i in range(1,c+1):
        cube[i] = i**3
    return cube

c= int(input("Enter a number :"))
print(cubic(c))

def find(s):
    word={}
    for i in s:
        word[i]=s.count(i)
    return word

s = input("Enter a name : ")
print(find(s))

def sq(d):
    f={}
    for i in range(1,d+1):
        f[i]=i**2
    return f
a=int(input("Enter a  number : "))
print(sq(a))

d = {}
name = input("Enter your name: ")
age = input("Enter Your Age: ")
fav_movies = input("your favourite movie is separated by comma(,) ").split(",")
fav_song = input("your favourite song is separated by comma(,) ").split(",")

d["Name"] = name
d["Age"] = age
d["fav_movies"] = fav_movies
d["fav_song"] = fav_song
for key,value in d.items():
    print(f"{key}:{value}")

