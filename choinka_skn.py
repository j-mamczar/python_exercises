# choinka

def choinka(n):
    times = n - 1
    star_multiple = 1
    for i in range(n):
        print(" " * times + "*" * star_multiple)
        times -= 1
        star_multiple +=2
    print(" " * (n-1) + "*")
    print(" " * (n-2) + "*" * 3)

# choinka(7)
# choinka(4)
choinka(10)