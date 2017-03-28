n = 0
while n < 5:
    n += 1
    print n

print '--------------------------'

# for loop seems better than while loop

for i in range(6):
    print i

print '--------------------------'

mysum = 0

for m in range(2, 9, 3):
    mysum += m

print mysum


print '--------------------------'

mysum = 0

for c in range(3, 100, 4):
    mysum += c
    if mysum > 30:
        break

print mysum


print '--------------------------'

for happy in range(5):
    if happy > 2:
        print 'hello world'
        print happy
        break
