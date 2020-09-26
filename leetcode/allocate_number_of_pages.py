

#Flipkart question
# Related Problems For Practice : Book Allocation Problem (GFG) Aggressive cow (spoj) Prata and roti (spoj) EKO (spoj) Google kickstart A Q-3 2020

# Painter Partition Problem
# 1482 Minimum Number of Days to Make m Bouquets 1283 Find the Smallest Divisor Given a Threshold 1231 Divide Chocolate 1011 Capacity To Ship Packages In N Days 875 Koko Eating Bananas Minimize 774 Max Distance to Gas Station 410 Split Array Largest Sum


#In this question we create a number line for the minimum number of books and maximum number  of books possible.
#If its valid we try to find a minimum number of books possible
#If invalid we know that we need to increase the number of books that we can allocate to the students.

def isvalid(mid):

    total=0
    students=1
    for i in range(len(arr)):

        total+=arr[i]
        if total>mid:
            students+=1
            total=arr[i]
        if students>k:
            return False
    return True

def  binarysearch(low,high):

    res=float("inf")

    while low <= high:
        mid = low + (high-low)//2

        if isvalid(mid):
            res=min(res,mid)
            high= mid-1
        else:
            low= mid+1
    return res

arr=[10,20,30,40]
k=2
low=0
high=sum(arr)
result=binarysearch(low,high)
print(result)