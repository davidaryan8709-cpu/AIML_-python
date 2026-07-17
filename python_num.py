import numpy as np
def square (number):
    return number * number
nums=[2,3,4,5,6]
square_Numbers=list(map(square,nums))
print(square_Numbers)