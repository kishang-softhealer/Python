#Q1
name = "jeo"
age =34
height = 6.2
print(f"Name : {name}, Age : {age}, Height : {height}")

#4Q2
M = 17
L = "19"
G = int(L)
print(M+G)

#Q3
x=5
y=5.0
z="5"

print(isinstance(x,int))
print(isinstance(y,float))
print(isinstance(z,str))

#Q4
name1,city,age1 = "jeo","ahemdabad",28
print(f"Name : {name1} , City : {city} , Age : {age1}")

#Q5
#way1
a=5
b=10
print("before Swap a is:",a, "b is:",b)

a = a+b
b = a-b
a = a-b

print("after Swap a is:",a, "b is:",b)

#way2
a1 = 5
b1 = 10

print("before Swap a is:",a1, "b is:",b1)

a1 = a1*b1 #50
b1 = a1//b1 #5
a1 = a1//b1 #10

print("after Swap a is:",a1, "b is:",b1)

#way3
a2 = 5
b2 = 10

print("before Swap a is:",a2, "b is:",b2)

a2,b2 = b2,a2

print("after Swap a is:",a2, "b is:",b2)
