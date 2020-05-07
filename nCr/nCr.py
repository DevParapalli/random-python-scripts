import factorial #we import previous script and its functions into this script

# we define a nCr function that takes 
def nCr(n,r):
    a = factorial.factorial(n) # this is how we call a function from a different script 
    b = factorial.factorial(r) # logic is similar to your program
    c = factorial.factorial(n - r)
    return(a/(b*c))


if __name__ == "__main__": #runs only when this program is called
    n = float(input("N = "))
    r = float(input("R = "))
    print("nCr with N = {}, and R = {} evaluates to {}".format(n,r,nCr(n,r)))