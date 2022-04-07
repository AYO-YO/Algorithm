t = int(input()) / 1000
h = int(t % 86400 / 3600)
m = int(t % 3600 / 60)
s = int(t % 60)
print(f'{h:02d}:{m:02d}:{s:02d}')
