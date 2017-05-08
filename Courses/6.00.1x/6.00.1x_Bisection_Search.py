cube = 0.05
epsilon = 0.001
numGuesses = 0
low = cube
high = 1
ans = (low + high)/2

while abs(ans**3 - cube) >= epsilon:
    numGuesses += 1
    print 'Guess No.'+str(numGuesses), 'low=', low, 'high=', high, 'ans=', ans
    if ans**3 > cube:
        high = ans
    else:
        low = ans
    ans = (low + high)/2

print 'The answer is', ans
