# function
def calc_sum (a,b):
    sum = a + b
    print (sum)
    return sum 
calc_sum(5,10)
    
# function defination
def calc_sum (a,b):  #parameters
    return a + b
sum = calc_sum(34,33) # function call arguments
print(sum)
    
    # average of 3 numbers
def calc_avg(a,b,c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg
calc_avg(1,2,3)


# Print function
print("appnacollege", end=" ") #sep = " "
print("ppoja rawat" ) #end = "\n"

# defalut value argument
def cal_prod(a=1, b=2):
    print(a * b)
    return a * b
cal_prod()


# Recursion

def show(n):
    if(n ==0):
        return
    print (n)
    show(n-1)
    show(3)

# Recrsion for factorial
def fact (n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n
print(fact(2))

# 
def fact (n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n
print(fact(4))