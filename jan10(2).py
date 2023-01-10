def square_list(l):
    square=[]
    for i in l:
        square.append(i**2)
    return square
rate = list(range(1,11))
print(square_list(rate))

def reverse(l):
    rev= l[::-1]
    return rev
a= [9,8,7,6,5]
print(reverse(a))

b = [9,8,7,6,5]
b.reverse()
print(b)

def back(l):
    ba=[]
    for i in range(len(l)):
        pop = l.pop()
        ba.append(pop)
    return ba
c=[9,8,7,6,5]
print(back(c))


def rest(l):
    khali=[]
    for i in range(len(l)):
        popped=l.pop()
        khali.append(popped)
    return khali
l=[9,8,7,6,5]

def fun(l):
    sq=[]
    for i in l:
        k = i[::-1]
        sq.append(k)
    return sq
l = ["kulwat","olkha","is","boy"]
print(fun(l))

def num(l):
    odd=[]
    even=[]
    final=[]
    for i in l:
        if i%2==0:
            odd.append(i)
        else:
            even.append(i)
        # k = i%2==0
        # m = i%2!=0
        # odd.append(m)
        # even.append(k)
        final = [odd, even]
    return final

y=[1,2,3,4,5,6,7,8,9,0]
print(num(y))

def common(l1,l2):
    output =[]
    for i in l1:
        if i in l2:
            output.append(i)
    return output

print(common([1,2,4,5], [1,5,8,3,8,]))

def same(l):
    count = 0
    for i in l:
        if type(i) == list:
            count = count + 1
    return count

o=[1.3,7,[2,4,6],"list",6,["hi"]]
print(same(o))
