a = int(input())
for b in range(1,a+1):
    for c in range(a-b):
        print(" ", end="")
    for d in range(b):
        print("*",end="")
    print()