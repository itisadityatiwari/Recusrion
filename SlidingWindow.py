'''This is Sliding window example
Find Maximum subarray sum of size k:3
Input: array=[2,5,1,8,2,9,1]
return maximum subarray sum of size 3'''
def maxisubarray(arr,k):
    i=0 #used to represent start
    j=0 #used to represent end
    sum_arr=0 #use to calculate sum of array
    maxi=0 #variable we use to store the maximum of sum, we will be returning this value
    while j<len(arr):
        sum_arr=sum_arr+arr[j]
        #print("sum" ,sum_arr)
        if j-i+1 < k:
            j+=1
        elif j-i+1 == k:
            maxi=max(maxi,sum_arr)
            sum_arr=sum_arr-arr[i] #substract a value from left, value from the right is added above in sum_arr=sum_arr+arr[j]
            i+=1 #remove pointer from left
            j+=1 #increment the pointer from right
        
    return maxi

print(maxisubarray([2,5,1,8,2,9,1],3))


