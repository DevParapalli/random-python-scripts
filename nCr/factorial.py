
def floor(x):
    y = x
    while y > 1:
        y = y - 1
    return(x - y + 1)

def factorial(x):
    floor_x = floor(x)
    fact = 1
    test_for_float = x - floor_x     
    if abs(x) != x:
        raise ValueError("Factorial for negative numbers isn't defined")
    elif test_for_float != 0.0:
        raise ValueError("Factorial for floating point numbers isn't defined")
    elif x == 0:
        return(fact)
    elif x == 1:
        return(fact)
    elif x > 1:
        x = int(x)
        for i in range(1,x+1): 
            fact = fact * i
        return(fact)

if __name__ == "__main__":
    pre_factorial = float(input("Enter a number for Factorial: "))
    print("Factorial for {} is".format(pre_factorial), factorial(pre_factorial))

  
  
