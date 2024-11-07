#1 Biggie Size
def biggie_size(list):
    for i in range(0,len(list)):
        if list[i]<0:
            list[i]="big"
    return list

print (biggie_size([1,2,-5,8,-9,10]))

#2 Count Positive
def count_positive(list):
    num=0
    for i in range(0,len(list)):
        if list[i]>0:
            num+=1
    list[len(list)-1] =num
    return list
print (count_positive([1,-5,7,8,9,5,-5]))          

#3 Sum Total
def sum_total(list):
    sum=0
    for i in range(0,len(list)):
        sum+=list[i]
    return sum
print (sum_total([1,2,3,4]))    

#4 Average
def average_nums(list):
    sum=0
    for i in range (0,len(list)):
        sum+=list[i]
        
    return sum/len(list)  
print (average_nums([1,2,3,4]))

#5 Length
def length(list):
    length_num=0
    for i in range (0 ,len(list)):
        length_num+=1
    return length_num
print (length([1,2,5,4,8,8]))    

#6 Minimum
def minimum(list):
    if len(list)==0:
        return False  
    else:
        min_num = list[0]
        for i in range(0,len(list)):
            if list[i]<min_num:
                min_num=list[i]
    return min_num
print (minimum([2,3,4,5]))

#7 Maximum
def maximum(list):
    if len(list)==0:
        return False
    else:
        max_num=list[0]
        for i in range(0,len(list)):
            if list[i]>max_num:
                max_num=list[i]
        return max_num
print (maximum([10,15,17,5,7]))      

#8 Ultimate Analysis
def ultimate_analysis(list):
    dictionary={
        "sum_total": sum_total(list),
        "average": average_nums(list),
        "minimum": minimum(list),
        "maximum": maximum(list),
        "length of list": length(list)
    }
    return dictionary   
print (ultimate_analysis([1,5,6,7,8,9]))

def reverse_list(list):
    left=0
    right=len(list)-1
    while left<right:
        list[left],list[right]=list[right],list[left]
        left+=1
        right-=1

    return list
print (reverse_list([5,6,7,8,9,7]))
             
            

        

        