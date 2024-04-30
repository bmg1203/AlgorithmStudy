# 백준 2309 Bronze I

a = []

for i in range(9):
  a.append(int(input()))

a.sort()
sum = 0

for i in range(len(a)):
  sum += a[i]

b = sum - 100

for i in range(9):
  for j in range(i, 9):
    if (a[i] + a[j]) == b and i != j:
      del a[i]
      del a[j - 1]
      break
  if (len(a) == 7):
    break

for i in range(len(a)):
  print(a[i])
