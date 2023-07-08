import math 
k=math.trunc(-5/2)
print(k)

ls1=[1,2,3]
ls2=[1,2,3]
print(id(ls1))
print(id(ls2))

ls2=ls1

print(id(ls1))
print(id(ls2))
print(ls1 is ls2)

x=2
y=4
print(y|x)

print(pow(2,5))
print(2**5)

def foo():
    return 5
x=10
print(x+foo())
x=None
y=None
print(x is y)
print(5+2*2)

ls=[11,2,3]
def foo(ls):
    ls.reverse()
    return ls
    
print(foo(ls))
for i in foo(ls):
    print(i)

import fractions
t=fractions.Fraction(3,12)  
print(t)

sett={1,2,2,2} 
print(sett)  

#user_weight_kilo = input('Please write your weight in kilograms:')
pound=2.2
#user_weight_pounds=pound*int(user_weight_kilo)
#print(user_weight_pounds)
#Write a program that asks the user for weight in kilograms and converts it to pounds. There are 2.2 pounds in a kilogram
s1={1,2,3,4}

s2={3,4,5,6}
print(s1.intersection(s2))

d1={"name":"Vardan", "age":33}
d2=d1.copy()
print(d2)
d2["name"]="Hayk"
print(d1)
print(d2)
#*****************************************************

d1.fromkeys("name")
print(d1.fromkeys("name"))

print(d1.fromkeys([1,2],"hi"))

print(d1.fromkeys([1,2],["hi","bye"]))

#*******************************************************
d1.get("name")
print(d1.get("name"))
print(d1.get("job"))

#print(d1["job"])

#*******************************************************
d5={"name": "Vardan", "age": "33"}
print(d5.items())

#*******************************************************
di={"name":"Bob","age":13,"job":"programmer","proffesion":"mathematics"}
print(di.pop("age"))
print(di.popitem())
print(di)
#********************************************************

import collections
print(collections.defaultdict(str,di))
#********************************************************

f = open("demofile.txt", "w")
print(f.write("Hello I am Mary"))


#*****************************************************

f = open("C:/Users/MERI/Desktop/Artashat.txt", "r")
print(f.read())

#f = open("demofile.txt", "x")
#print(f.ex())

#f = open("nnn.txt", "x")
#print(f.write("Hello"))

f = open("nnn.txt", "a")
print(f.write(", World"))
