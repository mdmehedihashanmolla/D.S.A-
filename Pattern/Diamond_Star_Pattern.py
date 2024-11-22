def Star_Pyramid(n):
    for i in range(n):
        print(" " * (n - i - 1), end="")
        print("*" *(2 * i + 1))


def Inverted_Star_Pyramid(n):
    for i in range(n,0,-1):
        print(" " * (n-i), end="")
        print("*" *(2 * i - 1))

Star_Pyramid(6)
Inverted_Star_Pyramid(6)
