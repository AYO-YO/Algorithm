light = {i: True for i in range(1, 1001)}


def switch(i):
    global light
    if light[i]:
        light[i] = False
    else:
        light[i] = True


for i in range(3, 1001, 3):
    switch(i)
for i in range(5, 1001, 5):
    switch(i)
for i in range(7, 1001, 7):
    switch(i)
c = 0
for i in range(1, 1001):
    if light[i]:
        c += 1
print(c)
