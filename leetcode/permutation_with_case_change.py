





def solve(ip,op):
    if len(ip) ==0:
        print(op)
        return
    if ip[0].isdigit():
        op1=op+ip[0]
        ip=ip[1:]
        solve(ip,op1)
    else:
        op1=op+ip[0].lower()
        op2=op+ip[0].upper()
        ip=ip[1:]
        solve(ip,op1)
        solve(ip,op2)



s="a1B2A"
op=""
solve(s,op)