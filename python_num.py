# import numpy as np
# def square (number):
#     return number * number
# nums=[2,3,4,5,6]
# square_Numbers=list(map(square,nums))
# print(square_Numbers)

# def lamba(num1):
#     list(map(lambda num:num*num,num1))

# num1=[1,2,3,4]
# print(lamba(num1))

from functools import reduce 
def sum_all(a,b):
    return a+b 
nums = [1,2,3,4]
sum = reduce(sum_all,nums)
print(sum)