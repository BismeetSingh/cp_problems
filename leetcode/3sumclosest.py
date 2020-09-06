#Three sum closest to target.
#The idea is to keep track of the minimum distance from the target value.
def solve(a,t):
    
    a.sort()
    i=0
    ans=set()
    diff=float("inf")
    while(i<len(a)):
        j=i+1
        k=len(a)-1
        while(j<k):
            sum=a[j]+a[k]+a[i]
            if sum==t:
                tmp=(a[i],a[j],a[k])
                ans.add(tmp)
                
            if sum>t:
                k-=1
            else:
                j+=1
        
        i+=1
    return ans


a=[-7,14,-7,8,-4,-4,-4,-4,-4]
t=0
print(solve(a,t))