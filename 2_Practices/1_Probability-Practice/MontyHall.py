import random

# test random
'''
a = [1, 2, 3]
n = 1000
a1 = 0
a2 = 0
a3 = 0

for i in range(n):
  r = random.sample(a, 1)
  if r == [1]:
        a1 = a1 + 1
  elif r == [2]:
        a2 = a2 + 1
  elif r == [3]:
        a3 = a3 + 1

print float(a1)/float(n)
print float(a2)/float(n)
print float(a3)/float(n)
'''


def montyhall(Dselect, Dchange):
    Dcar = random.randint(1, 3)
    if Dcar == Dselect and Dchange == 0:
        return 1
    elif Dcar == Dselect and Dchange == 1:
        return 0
    elif Dcar != Dselect and Dchange == 1:
        return 1
    else:
        return 0

win = 0
for i in range(100000):
    ds = random.randint(1, 3)
    dc = random.randint(0, 1)
    win += montyhall(ds, dc)

print(float(win)/100000)
