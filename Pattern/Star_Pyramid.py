def Star_Pyramid(n):
    for i in range(n):
        print(" " * (n - i - 1), end="")
        print("*" *(2 * i + 1))

Star_Pyramid(6)