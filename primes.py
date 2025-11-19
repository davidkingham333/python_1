import math
#git changes

def prime_nums(n) -> int:
    if n<=1:
        print("not a prime number")
        return 0
    elif n==2:
        print("prime number")
        return 1
    elif n%2==0:
        print("not a prime number")
        return 0
    else:
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n%i==0:
                return 0
        print("prime number")
        return 1


try:
    inp=int(input("enter a number:"))
    if prime_nums(inp):
        print(f"prime number{prime_nums}")
    else:
        print("this is not prime number")

except ValueError:
    print("enter a valid integer")


