# 백준 1924 Bronze I

# 1번 방법
x, y = map(int, input().split())


def Year(y):
  if (y % 7 == 0):
    print('SUN')
  elif (y % 7 == 1):
    print('MON')
  elif (y % 7 == 2):
    print('TUE')
  elif (y % 7 == 3):
    print('WED')
  elif (y % 7 == 4):
    print('THU')
  elif (y % 7 == 5):
    print('FRI')
  elif (y % 7 == 6):
    print('SAT')


if (x == 1):
  Year(y)
elif (x == 2):
  y += 31
  Year(y)
elif (x == 3):
  y += 59
  Year(y)
elif (x == 4):
  y += 90
  Year(y)
elif (x == 5):
  y += 120
  Year(y)
elif (x == 6):
  y += 151
  Year(y)
elif (x == 7):
  y += 181
  Year(y)
elif (x == 8):
  y += 212
  Year(y)
elif (x == 9):
  y += 243
  Year(y)
elif (x == 10):
  y += 273
  Year(y)
elif (x == 11):
  y += 304
  Year(y)
elif (x == 12):
  y += 334
  Year(y)

# 2번 방법
a = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(x - 1):
  y += b[i]
  i += 1

print(a[y % 7])
