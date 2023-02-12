num = int(input())
numlist = list(map(int, input().split()))

max = numlist[0]
min = numlist[0]

for i in numlist[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i
print(min, max)