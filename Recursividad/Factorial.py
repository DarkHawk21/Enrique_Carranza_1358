def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial (n-1)

def main():
    print(factorial(9))

main()