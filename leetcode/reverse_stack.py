

def insert_stack(stack,element):
    if len(stack)==0:
        stack.append(element)
    else:
        val=stack.pop()
        insert_stack(stack,element)
        stack.append(val)

def reverse_stack(stack):
    if len(stack)>0:
        
        val=stack.pop()
        reverse_stack(stack)
        insert_stack(stack,val)


stack=[5,6,7,8,9,1,7,9,10,14]
reverse_stack(stack)
print(stack)