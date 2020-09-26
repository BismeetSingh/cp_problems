

#Josephus problem relates to find the safest position to stand when kth person is being killed from a group of n people standing in a circle.0  
def solve(arr,k,index):
    if len(arr)==1:
        print(arr[0])
        return
    index = (index+k)%len(arr)
    arr.pop(index)
    solve(arr,k,index)


n=5
k=3
arr=[]
for i in range(1,n+1):
    arr.append(i)
k=k-1
solve(arr,k,0)