"""https://nanti.jisuanke.com/t/T1185"""

books = {}
n = int(input())
for i in range(n):
    isbn, author = input().split()
    for a in author:
        if a not in books:
            books[a] = [isbn]
        else:
            books[a].append(isbn)

books = sorted(books.items(), key=lambda x: (len(x[1]), -ord((x[0]))), reverse=True)
print(books[0][0])
print(len(books[0][1]))
for i in books[0][1]:
    print(i)
