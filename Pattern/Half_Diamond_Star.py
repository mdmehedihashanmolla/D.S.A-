def Half_Diamond_Star(n):
    for i in range(1, n + 1):
        print("*" * i)
    
    for i in range(n - 1, 0, -1):
        print("*" * i)

Half_Diamond_Star(5)
