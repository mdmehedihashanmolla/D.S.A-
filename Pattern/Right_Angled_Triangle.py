def Right_Angled_Triangle(n):
    for i in range(n+1):
        for j in range(i):
            print("*", end="")
        print()

Right_Angled_Triangle(6)