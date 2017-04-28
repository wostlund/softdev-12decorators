import time

def wrapper( function ):
    def inner( *args ):
        ans =  function( *args )
        print function.func_name, args
        return  ans
    return inner

def timer( function ):
    def inner( args ):
        timeInit = time.time()
        ans = function( args )
        print "Run Time:", time.time() - timeInit
        return ans
    return inner

@wrapper
def fibonacci(num):
    if num == 1 or num == 2:
        return 1
    return fibonacci(num - 2) + fibonacci(num - 1)

def swap(i, j, array):
    k = array[i]
    array[i] = array[j]
    array[j] = k
    return array

#@timer
def insertionSort( array ):
    for i in range(len(array))[1 : ]:
        while i != 0 and array[i] < array[i - 1]:
            array = swap(i - 1, i, array)
            i -= 1
    return array

ans = fibonacci(5)
print "The fifth element of the fibonacci sequence is: "+ str(ans) + "\n\n"


func = timer(insertionSort)
ans2 = func([25, 354,435,54,54,6354,35,5635,43,4,534325,56,2,343,214,243,1,24,56,7,89,78,62,5,67,90,9,543,67,9,87])

print "[25, 354, 435, 54, 54, 6354, 35, 5635, 43, 4, 534325, 56, 2, 343, 214, 243, 1, 24, 56, 7, 89, 78, 62, 5, 67, 90, 9, 543, 67, 9, 87] SORTED is: ", ans2
