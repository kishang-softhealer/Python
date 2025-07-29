# Question 11: Word Split from Dictionary
# Have the function WordSplit(strArr) read the array of strings stored in strArr, which will contain 2 elements: the first element will be a sequence of characters, and the second element will be a long string of comma-separated words in alphabetical order, that represents a dictionary.

# Your goal is to determine if the first element in the input can be split into two words, where both words exist in the dictionary provided in the second input.
# ●​ Input: ["hellocat", "apple,bat,cat,goodbye,hello,yellow,why"]
# ●​ Output: ["hello", "cat"]
# If there is no valid way to split the string, return "not possible".



A1 =["hellocat", "apple,bat,cat,goodbye,hello,yellow,why"]

def WordSplit(strArr):
  B1 = strArr[0]
  b3 = strArr[1].split(",")
  b4 = []
  for i in b3:
    if B1 in b3:
      b4.append(i)
    else:
      print("not")  
      break  
  print(b3)     
WordSplit(A1)