"""https://nanti.jisuanke.com/t/T1171"""

n = int(input())
persons = {}
for i in range(n):
    s = input().split()
    if s[1] != "0":
        for j in s[2:]:
            if j in persons:
                persons[j].add(s[0])
            else:
                persons[j] = {s[0]}
persons = sorted(persons.items(), key=lambda x: (len(x[1]), -int(x[0])), reverse=True)
print(persons[0][0])
print(' '.join(sorted(list(persons[0][1]))))
