


def insert(arr,temp):
    if len(arr)==0 or arr[-1]<=temp:
        arr.append(temp)
    else:
        val=arr.pop()
        insert(arr,temp)
        arr.append(val)


def sort(arr):

    if len(arr)>0:

        value=arr.pop()
        sort(arr)
        insert(arr,value)
        # print(value)

arr=[5,4,3,2,1]
sort(arr)
print(arr)