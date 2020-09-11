
#Recursion tree is the root of the solution.
#References: https://www.youtube.com/watch?v=eyCj_u3PoJE&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=17
def generate_balanced_parantheses(open,close,op):    
    if open==0 and close==0:
        print(op)
        return
    if open!=0:
        op1=op+"("
        generate_balanced_parantheses(open-1,close,op1)
    if close>open:
        op2=op+")"
        generate_balanced_parantheses(open,close-1,op2)
   

n=20
open=n
close=n
generate_balanced_parantheses(open,close,"")