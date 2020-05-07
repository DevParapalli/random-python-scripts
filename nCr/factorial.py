# The floor function is basically the Greatest Integer function for python, 
# this is a very novice way to do GIF

def floor(x):
    y = x
    while y >= 1:  # we subtract 1 from the number until it has only fractional part or is zero,
        y = y - 1  # then we subtract this from the original number to get the integer (its type is float but ok)
    return(x - y)

# 

def factorial(x):
    floor_x = floor(x) # basically gif(x)
    fact = 1 
    test_for_float = x - floor_x  # this is the fractional part of x 
    if abs(x) != x:
        raise ValueError("Factorial for negative numbers isn't defined") # we define a ValueError to provie a proper way for a function to handle exceptions
    elif test_for_float != 0.0: # if there exists a fractional part to x (!= means not equals to) then raise exception
        raise ValueError("Factorial for floating point numbers isn't defined") # 
    elif x == 0: #  basic stuff
        return(fact) # return statements give values when fucntions are called while assigned to variables
    elif x == 1:
        return(fact)
    elif x > 1: # this is a very naive method to calculate factorials  
        x = int(x)
        for i in range(1,x+1): 
            fact = fact * i
        return(fact)
    else:
        raise UnknownError("IDK WHERE THIS WENT WRONG")
if __name__ == "__main__": # this code block is run only when this program is run on its own.
    pre_factorial = float(input("Enter a number for Factorial: ")) # we convert to float to do float arithmetic in the floor and factorial functions
    print("Factorial for {} is".format(pre_factorial), factorial(pre_factorial)) #string.format() function is a important function to place varables inside preformed strings

  
  
