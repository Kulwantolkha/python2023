def user_info(first_name,last_name="Olkha",age=19):
    print(f"your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")

user_info("Kulwnat")

fruits =["apple", "banana"]
fruits2 = ["mango", "gavava"]
fruits.insert(0, "oranges")
fruits1= fruits+fruits2
print(fruits1)
print(fruits)
fruits.extend(fruits2)
print(fruits)
fruits.append(fruits2)
print(fruits)
elements =["sodium","magnisum","aluminium","silicon","phosphorus"]
elements.pop()
print(elements)
elements.pop(3)
print(elements)
del elements[2]
print(elements)
elements.remove("sodium")
print(elements)
if "aluminimum" in elements:
    print("Yes")
else:
    print("No")
elements.sort()
print(elements)
numbers=[1,23,45,6,24,6,2]
print(sorted(numbers))
numbers.clear()
print(numbers)
print(fruits == fruits2)
print(fruits is fruits2)
for i in elements:
    print(i)

num =[[1,2,3],[4,5,6],[7,8,9]]
for number in num:
    print(number)

for numb in num:
    for i in numb:
        print(i)

print(num[1][1])

range = list(range(10,21))
print(range)
print(range.index(15))

def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(range))

number=[24,446,4363,6457]
print(max(number))
print(min(number))
def greater_difference(l):
    return max(l)-min(l)

print(greater_difference(number))
