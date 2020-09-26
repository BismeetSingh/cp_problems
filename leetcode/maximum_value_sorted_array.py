#User function Template for python3
# class Solution:
#Similar to finding the peak.
def findMaximum(arr, n):
    
    low=0
    high=n-1
    
    if len(arr)==1:
        return arr[0]

    while low<=high:
        
        mid = low + (high-low)//2

        # print(mid)
        
        # next = (mid+1)
        
        # prev = (mid-1)
        
        if (mid)>0 and (mid)<n-1:

            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                
                return arr[mid]
            # break
        
            if arr[mid]<arr[mid+1]:
                
                low=mid+1
                
            else:
                high=mid-1

        elif mid==0:
            if arr[0]>arr[1]:
                return arr[0]
            else:
                return arr[1]

        elif mid==n-1:
            if arr[-1]>arr[-2]:
                return arr[-1]
            else:
                return arr[-2]


            

arr=[1,3,8,9]
n=len(arr)

print(findMaximum(arr, n))

