
# Question 13: Reverse Only Vowels in a String
# Given a string, your task is to reverse only the vowels in the string.

# ●​ Input: hello
# ●​ Output: holle
# ●​ Input: hello world
# ●​ Output: hollo werld

v = "aeiouAEIOU"

W = "hello"

list_str = list(W)

i,j = 0,len(list_str)-1
while i<j:
  if list_str[i] not in v:
    i += 1
  if list_str[i] not in v:
     j -=1  
  else:
    list_str[i],list_str[j]   =  list_str[j],list_str[i]  
    i += 1
    j -=1 
result1 =  "".join(list_str)
print(result1)