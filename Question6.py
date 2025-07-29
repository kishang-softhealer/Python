list_mul =[[1, 2, 3], [4, 5], [6, 7, [8, 9]]]
# N = itertools.chain([[1, 2, 3], [4, 5], [6, 7, [8, 9]]])
# K = list(N)
# print(K)

result = []
def rec(le):
  for i in le:
    if type(i) is list:
      rec(i)
    else:
      result.append(i)  
  return result    
print(rec(list_mul))