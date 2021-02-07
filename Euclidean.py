from math import *

def gcd(a, b):
    #Basic euclidean algorithm -> greatest common denominator
    #print(str(a) + " and " + str(b))
    if a == 0:
        return b
    return gcd(b%a, a)

def extgcd(a, b):
    #Extended euclidean algorithm -> ax + by = gcd(a, b)
    if a == 0 :   
        return b, 0, 1
    print(b%a, a)
    gcd, x1, y1 = extgcd(b%a, a)
    print(str(gcd) + " " + str(x1) + " " + str(y1))
    x = y1 - (b//a) * x1  
    y = x1
     
    return gcd, x, y 
