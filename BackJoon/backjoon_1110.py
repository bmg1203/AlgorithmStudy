#백준 1110 Bronze 1

n = int(input())
num = n
i = 0

while (True):
  a = n % 10  #1의 자리수
  b = n // 10  #10의 자리수
  c = a + b
  result = a * 10 + c % 10
  i += 1
  n = result

  if (result == num):
    break

print(i)
