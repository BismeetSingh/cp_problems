
    buildings=[2,3]
    left_stack=[]
    right_stack=[]
    left_ans=[]
    right_ans=[]
    #NSL will go from start to end
    #NSR will go from end to start

    #Stacks will hold pairs of indices and values at indices(tuple).

    left=0


    while left<len(buildings):

        while len(left_stack)>0 and left_stack[-1][1]>=buildings[left]:
            left_stack.pop()

        if len(left_stack)>0:
            # difference=left-left_stack[-1][0]
            left_ans.append(left_stack[-1][0])
        else:
            left_ans.append(-1)
        left_stack.append((left,buildings[left]))
        left+=1

    right=len(buildings)-1

    while right>=0:

        while len(right_stack)>0 and right_stack[-1][1]>=buildings[right]:
            right_stack.pop()

        if len(right_stack)>0:
            # difference=left-left_stack[-1][0]
            right_ans.append(right_stack[-1][0])
        else:
            right_ans.append(len(buildings))
        right_stack.append((right,buildings[right]))
        right-=1
    right_ans=right_ans[::-1]
    print(left_ans)
    print(right_ans)
    ans=0
    for i in range(len(right_ans)):
        #Difference of nsr and nsl
        diff=(right_ans[i]-left_ans[i]-1)*buildings[i]
        ans=max(ans,diff)
    print(ans)