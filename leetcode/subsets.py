

def subsets(s,op):
    # print(s)
    if len(s) ==0:
        print(op)
        return
    op1=op
    op2=op+s[0]
    s=s[1:]
    subsets(s,op1)
    subsets(s,op2)  
s="123"
op=""
op+=s[0]
s=s[1:]
subsets(s,op)