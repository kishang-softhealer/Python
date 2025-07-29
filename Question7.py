# Question 7: 


d1 = {'a': 1, 'b': 2, 'c': 3}

def revers_dict(d):
  return{v:k  for k,v in d.items()}
print(revers_dict(d1))

