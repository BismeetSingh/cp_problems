

def delete_middle_element(stack,n,k):

    if n>((k//2)+1):
        tmp=stack.pop()
        delete_middle_element(stack,n-1,k)
        stack.append(tmp)
    else:
        stack.pop()


stack=[1,2,23,4,15,6,7,18,9,10,11,12,13,14] 
delete_middle_element(stack,len(stack),len(stack))
print(stack)