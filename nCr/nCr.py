import factorial

def nCr(n,r):
    a = factorial.factorial(n)
    b = factorial.factorial(r)
    c = factorial.factorial(n - r)
    return(a/(b*c))


if __name__ == "__main__":
    n = float(input("N = "))
    r = float(input("R = "))
    print("nCr with N = {}, and R = {} evaluates to {}".format(n,r,nCr(n,r)))