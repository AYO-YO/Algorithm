mp = {2: 1, 3: 2, 4: 1, 5: 4, 6: 5, 7: 4, 8: 1, 9: 2, 10: 9, 11: 0, 12: 5, 13: 10, 14: 11, 15: 14, 16: 9, 17: 0, 18: 11,
      19: 18, 20: 9, 21: 11, 22: 11, 23: 15, 24: 17, 25: 9, 26: 23, 27: 20, 28: 25, 29: 16, 30: 29, 31: 27, 32: 25,
      33: 11, 34: 17, 35: 4, 36: 29, 37: 22, 38: 37, 39: 23, 40: 9, 41: 1, 42: 11, 43: 11, 44: 33, 45: 29, 46: 15,
      47: 5, 48: 41, 49: 46}

ls = [i for i in range(1, 10 ** 4)]
for i in range(2, 10):
    ls = list(filter(lambda x: x % i == mp[i], ls))
print(ls)
ls = [i for i in range(ls[0], 10 ** 9, ls[1] - ls[0])]
for i in range(10, 20):
    ls = list(filter(lambda x: x % i == mp[i], ls))
print(ls)
ls = [i for i in range(ls[0], 10 ** 13, ls[1] - ls[0])]
for i in range(20, 30):
    ls = list(filter(lambda x: x % i == mp[i], ls))
print(ls)
ls = [i for i in range(ls[0], 10 ** 17, ls[1] - ls[0])]
for i in range(30, 50):
    ls = list(filter(lambda x: x % i == mp[i], ls))
print(ls)
