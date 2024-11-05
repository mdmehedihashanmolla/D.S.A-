def Number_Pyramid_II(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i, end="")
        print()
Number_Pyramid_II(5)