# 백준 1546 Bronze I

n = int(input())
a = list(map(int, input().split()))

maxv = max(a)
sum = 0
for i in range(n):
  sum += a[i] / maxv * 100
  i += 1

avg = float(sum / n)
print(avg)
