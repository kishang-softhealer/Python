# Question 2
l1 = [("Alice", 25), ("Bob", 35), ("Charlie", 30)]
l2 = []

for i in range(len(l1)):
  if l1[i][1] >= 30:
    l2.append(l1[i][0])
print(l2)   