paper = input()
width = 1189
height = 841
count = int(paper[1])
while count > 0:
    if width < height:
        width, height = height, width
    width //= 2
    count -= 1
if width < height:
    width, height = height, width
print(width)
print(height)
