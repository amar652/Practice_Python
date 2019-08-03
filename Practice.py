num=int(input("Enter a Number:"))
for i in range (num):
    for j  in range(num-1):
            print(" ",end="")
    for j in range(i+1):
            print("* ",end="")
    print()
    num=num-1