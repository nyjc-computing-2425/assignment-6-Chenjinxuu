from datetime import datetime
import time


# Part 1
def clock(n):
    """
    Parameter:
    ----------
    int 
        the number of seconds for the clock to count
    Returns
    -------
    string
        every updated time per second over n seconds
    """
    # Your code here
    a = 0
    while a < n:
       a = a + 1
       print(str(datetime.now())[11:19], end = "\r")
       time.sleep(1)
#clock(60)
    #HH:MM:SS

# Part 2
def lcm(a, b):
    """
    Parameters'
    ----------
    int 
        a and b
    Returns
    -------
    int
        the lcm of integer a and b
    
    """
    # Your code here
    new_a = a
    new_b = b
    c = b
    if a == b:
        return a
    else:
        if a > b:
            while new_b < new_a:
                new_b += b
                while new_a < new_b:
                    new_a += a
            return new_a 
        else:
            while new_a < new_b:
                new_a += a
                while new_b < new_a:
                    new_b += b
            return new_a



# Part 3

def gcf(a, b):
    """
    Parameters
    ----------
    int
        2 integers a and b, a should be greater than b
    Returns
    -------
    int
        the GCF of the 2 integers
    """
    # Your code here
    if a == b:
        return a
    else:
        if b == 0:
            return a
        else:
            while b != 0:
                r = a%b
                a = b
                b = r
        return a

