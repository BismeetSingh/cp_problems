
def merge(arr,l,mid,h):
    global swaps
    print(swaps)
    n1=mid-l+1
    n2=h-mid
    L=[0]*n1
    R=[0]*n2  
    for i in range(n1):
        L[i] =arr[l+i]
    for i in range(n2):
        R[i] =arr[mid+1+i]
    i=0
    j=0
    k=l
    while (i<n1 and j<n2):
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
            swaps+=(n1-i)

        k+=1
    while(i<n1):
        arr[k]=L[i]
        i+=1
        k+=1
    
    while(j<n2):
        arr[k]=R[j]
        j+=1
        k+=1

    print(arr)
def merge_sort(arr,low,high):
    if low < high:
        mid =(low + high)//2
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)
        merge(arr,low,mid,high)
        # print(arr)

swaps=0
arr=[3,1,2]
merge_sort(arr,0,len(arr)-1)
print(arr)
print(swaps)