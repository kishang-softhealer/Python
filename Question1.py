# Question 1
def second_largest(l):
  ss = set(l)
  ll = list(ss)
  ll.sort(reverse=True)
  print(ll[1])
 
# l = [10, 20, 4, 45, 99]
l = [5, 10, 10]
second_largest(l)