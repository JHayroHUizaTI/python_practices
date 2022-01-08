def square_of_star(n):
    i = 0
    while i < n:
        stars = ""
        j = 0
        while j < n:
            stars += "* "
            j += 1
        print(stars)
        i += 1


n = int(input("cual es el numero: "))

square_of_star(n)
