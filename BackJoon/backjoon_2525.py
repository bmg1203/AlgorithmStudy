A, B = map(int, input().split())
C = int(input())

if (B + C >= 60):
    m = (B + C) // 60
    n = (B + C) % 60
    B = n
    A += m
else:
    B += C

if (A >= 24):
    A %= 24

print(A, B)