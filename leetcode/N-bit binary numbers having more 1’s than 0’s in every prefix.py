def solve(zeros,ones,N,answer):
        if N==0:
            ans.append(answer)
            return
        op1=answer+"1"
        solve(zeros,ones+1,N-1,op1)
        if zeros+1<=ones:
            op2=answer+"0"
            solve(zeros+1,ones,N-1,op2)
            
ans=[]  
def NBitBinary(N):
    
    current="1"
    solve(0,1,N-1,current)
    print(ans)
NBitBinary(2)