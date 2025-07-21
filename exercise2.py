'''Write a program to take two numbers from the user and perform all arithmetic operations (addition, subtraction, multiplication, division, modulus, floor division, exponentiation) on them.'''

print("Enter First Number :")
num1 = float(input())
print("Enter Second Number :")
num2 = float(input())

sum = num1+num2
sub = num1-num2
mul = num1*num2
div = num1/num2
fdiv = num1//num2
mod = num1%num2
exo = num1**num2

print(f"addition of {num1} and {num2} is:" ,sum )
print(f"subtraction of {num1} and {num2} is:" ,sub)
print(f"multiplication of {num1} and {num2} is:" ,mul)
print(f"division of {num1} and {num2} is:" ,div )
print(f"modulus of {num1} and {num2} is:" ,mod )
print(f"floor divisionof {num1} and {num2} is:" ,fdiv )
print(f"exponentiation of {num1} and {num2} is:" ,exo )


'''Write a program to check:
Whether a given element is in the list or not (membership)
Whether two variables are referring to the same object (identity)'''

language =["Python", "Java", "JavaScript", "C++", "C#", 
           "PHP", "Ruby", "Swift", "Go","Rust"]

for i in language:
    if "Swift" in i:
        print("Swift in language")
    else:
        print("Swift is not in language")  
        break 

x = "Python"
y = "java"
z = x
w = "java"
print(x is y)
print(y is z)
print(x is z)
print(y is w)
print(y == w)

list1 = ["Python", "Java"]
list2 =["JavaScript", "C++"]
list3 = list1
list4 = ["Python", "Java"]

print(list1 is list2)
print(list2 is list3 )
print(list1 is list3 )
print(list1 is list4 )
print(list1 == list4 )


''''Given a list: numbers = [10, 20, 30, 40, 50]
Print:
First three elements
Reverse the list
Replace 2nd element with 25
'''

numbers =[10,20,30,40,50]
print(numbers[0:3])
numbers.reverse()
print(numbers)
numbers[1] = 25
print(numbers)

'''9. Count Frequency of Elements in a List
Input: [1, 2, 2, 3, 3, 3, 4]
	Output: {1:1, 2:2, 3:3, 4:1}'''       


list5 = [1, 2, 2, 3, 3, 3, 4]


k = {i: list5.count(i) for i in set(list5)}
print(k)

"""Write a program to take two sets and:
Find common elements
Find elements only in the first set
Combine both sets (union)
"""

set1 = {1,2,3,4,5}
set2 = {6,8,7,1,2,4,9}
set3 = set1.intersection(set2)
print(set3)
set4 = set1.difference(set2)
print(set4)
set5 = set1.union(set2)
print(set5)

"""Find Unique Words from a Sentence
Input: "python is fun and python is powerful"
Output: {'fun', 'powerful', 'and'}
(Hint: Use sets and string methods)
"""

str = "python is fun and python is powerful"
str = str.split()
# print(str)
s1 =set()
for i in str:
 if str.count(i) == 1:
     s1.add(i)
print(s1)




"""Dictionary Merge with Value Sum Given:
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 100, 'd': 400}
Output: {'a': 400, 'b': 300, 'c': 300, 'd': 400}
"""
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 100, 'd': 400}

d3 = {}
for key, value in d1.items():
    d3[key] = value

for key, value in d2.items():
    if key in d3:
        d3[key] += value
    else:
       d3[key] = value
print(d3)

# d3 ={}
# for key in d1.keys()|d2.keys():
#     d3[key] = d1.get(key,0)+d2.get(key,0)
# print(d3)
  