def findTwoElement(nums): 
    for i in range(len(nums)):
        n=len(nums)
        pos=nums[i]-1
        while 1<=nums[i]<=n and nums[i]!=nums[pos]:
            nums[i],nums[pos]=nums[pos],nums[i]
            pos=nums[i]-1
    for i in range(len(nums)):
        if (i+1)!=nums[i]:
            print(i+1)
arr =[3,4,-7,1]
findTwoElement(arr)
print(arr)