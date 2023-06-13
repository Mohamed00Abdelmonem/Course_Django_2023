# Python Task Level 1 :



# 1. Create a python function that takes 2 numbers x,y and prints 2 lists containing the odd and even numbers in
# the x,y range


# def numbers(start,end):
     
    ################################# list comprhanchan ################################

    # even = [int(i) for i in range (start,end+1) if i%2==0 ]
    # odd = [int(i) for i in range (start,end+1) if i%2 !=0 ]
    # print(f"even = {even}")
    # print (f"odd =  {odd}")

# print(numbers(2,9))


    ####################### the normal way #################################


#     even = []
#     odd = []
#     for i in range(start, end+1):
#         if i % 2 == 0 :
#             even.append(i)    
#         else:
#             odd.append(i)
#     return(even,odd)


# even,odd= numbers(2,9)
# print(f"enve =  {even}")   
# print(f"odd =  {odd}")   






# 2. Create a python function that takes 2 numbers x,y and prints all the numbers between 1 and 100 than can
# be divided on x,y


    ################################# list comprhanchan ################################


# def divided_by_x_and_y(x,y):

    # var = [int(i) for i in range(1, 101) if i % x == 0 and i % y == 0]
    # return var



    ####################### the normal way #################################

#     value = []
#     for i in range(1,101):
#         if i % x ==0 and i % y ==0 :
#             value.append(i)
#     return value
        

# print(divided_by_x_and_y(3,5))

