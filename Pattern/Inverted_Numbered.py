def Inverted_Numbered(n):
    for i in range(n+1,1,-1):
        for j in range(1,i):
            print(j, end="")
        print()

Inverted_Numbered(5)