import numpy as np
import random

def base10(x):
    x = [int(x) for x in str(x)]
    p = len(x) - 1
    y = []
    
    for i in range(len(x)):  
        power = 2 ** (p)
        p =p - 1
        y.append(power)
    return np.dot(np.array(x), np.array(y))


x = input("Enter base 2 number: ")
print(base10(x))
