high = 60405
up = 105
down = 35
day = 0
while high > 0:
    day += 1
    high -= up
    if high <= 0:
        break
    high += down
print(day)
