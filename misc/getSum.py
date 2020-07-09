# Instead of 
def getSum(piece):
    if len(piece)==0:
        return 0
    else:
        return piece[0] + getSum(piece[1:])


print (getSum([1,3,5,7,9]))

# cant we do this..?
def myGetSum(list_object):
    if len(list_object) == 0:
        return(0)
    else:
        myvar = 0
        for i in range(len(list_object)):
            myvar += list_object[i]
        return(myvar)

print (myGetSum([1,3,5,7,9]))