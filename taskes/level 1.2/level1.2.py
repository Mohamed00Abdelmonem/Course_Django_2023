# Python Task Level 1 :



# 1. Create a python function that takes 2 numbers x,y and prints 2 lists containing the odd and even numbers in
# the x,y range


def numbers(start,end):
    even = [int(i) for i in range (start,end+1) if i%2==0 ]
    odd = [int(i) for i in range (start,end+1) if i%2 !=0 ]
    print(f"even = {even}")
    print (f"odd =  {odd}")
    # for i in range(start,end+1):
    #     if i % 2 == 0 :
    #         print (i)
    #     elif i % 2 != 0 :
    #         print(i)    
numbers(2,9)