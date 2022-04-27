ls=[]

for i in range(5):
    ls.append(input().split())

ls[1],ls[4]=ls[4],ls[1]

for l in ls:
    for j in l:
        print(f"{j:<5}",end="")
    print()
