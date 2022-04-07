sleep = 22 * 3600 + 28 * 60 + 45
awake = 6 * 3600 + 24 * 60 + 26
t = awake - sleep + 24 * 3600

print(t)

h = t // 60 // 60
m = t // 60 % 60
s = t % 60
print(h, m, s)
