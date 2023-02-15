a = int(input())
for b in range(1,a+1):
    for c in range(a+1-b):
        print("*", end="")
    print()