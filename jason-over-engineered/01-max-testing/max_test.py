
def max(*args): # search: python variable number of args
    # search: python local variable
    # search: python null
    toReturn = None 
    pos = 0
    for arg in args: # search: python foreach
        #search: python check if argument comparable
        if(type(arg) not in [int,float]):
            #search: python throw error
            raise ValueError(f"arg '{arg}' of type '{type(arg)}' in argument position '{pos}' is not a number.  Only numbers are supported.  ")
        pos +=1
        # search: python equality
        if(toReturn == None) or (toReturn < arg ):
            toReturn = arg
    if toReturn == None :
            raise ValueError("No input to function")
    return toReturn



# search: pytest  
# pytest is a python unit testing framework.  it will run any function that starts with "test_".  also it integrates with visual studio test explorer.
def test_hello():
    print("hi world")

def test_failureExample():
    myMax = max()
    print("will not get here.  will throw first")

def test_basic():
    myMax = max(1,4,8,0,-10)
    if myMax != 8:
        raise AssertionError("unexpected result")

def test_invalidArg():
    # search: python catch error
    try:
        myList = [2,4,"1",-1]
        #search: python list as *args
        myMax = max(*myList);
        print(myMax)
        raise AssertionError("expected to fail due to string")
    except ValueError:
        print("caught ok");


