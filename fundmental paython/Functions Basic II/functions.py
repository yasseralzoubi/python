# #1
# def a(num):
#     new_list=[]
#     for i in range(num,-1,-1):
#         new_list.append(i)
#     return new_list
# print(a(5))
# #2

# def Print_and_return(a_list):
#     print(a_list[0])
#     return (a_list[1])
# Print_and_return([4,5])   
#  #3       
# def first_plus_length(num):
#     return num[0] + len(num)
# print(first_plus_length([5,6,7,8,9]))
# 4
# def Values_greater_than_secound(list):
#     newList=[]
#     counter=0
#     for i in list:
#         if len(list)<2:
#             return False
#         if i > list[1]:
#             newList.append(i)
#             counter+=1
        
#     print(counter)
#     return newList 



# print(Values_greater_than_secound([1,2,3,4,5]))
# print(Values_greater_than_secound([1]))

# def Length_and_value(size,value):
#     return [value] * size
# print(Length_and_value(4,7))    


def repat(size,value):
    mylist=[]
    for i in range(0,size):
        mylist.append(value)

    return mylist

print(repat(4,7))