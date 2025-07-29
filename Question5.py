# Question 5: 

# ●​ Input: [1, 2, 3, 4, 5, 6], 3
# ●​ Output: [4, 5, 6, 1, 2, 3]

list4 =  [1, 2, 3, 4, 5, 6]
def rotate_list(n):
  list4 =  [1, 2, 3, 4, 5, 6]
  list5 = list4[n:]
  for i in list4:
    list5.append(i)
    if i ==n:
     break      
  print(list5)
rotate_list(3) 