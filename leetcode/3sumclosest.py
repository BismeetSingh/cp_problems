#Three sum closest to target.
#The idea is to keep track of the minimum distance from the target value.

def threeSumClosest(a, t):
    if not a:
        return 0
    a.sort()
    i=0
    ans=0
    indices=None
    value=None
    diff=float("inf")
    while(i<len(a)):
        j=i+1
        k=len(a)-1
        while(j<k):
            sum=a[j]+a[k]+a[i]
            #Check whether the new difference is less than the existing difference
            if abs(t-sum)<abs(diff):
                diff=abs(sum-t)
                ans=sum
                indices=(i,j,k)
                value=(a[i],a[j],a[k])
            if sum>t:
                k-=1
            else:
                j+=1
        
        i+=1
    return ans,indices,value



a=[-7,14,-7,8,-4,-4,-4,-4,-4]
t=89
print(threeSumClosest(a,t))