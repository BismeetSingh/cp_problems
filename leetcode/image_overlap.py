class Solution:
    
    def calculateOnes(self,A):
        c=0
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i][j]==1:
                    c+=1
        return c


    def calculateOnesRowColumn(self,l):
        c=0
        tmp=[]
        c1=[]
        for i in range(len(l)):
            c=0
            for j in range(len(l)):
                if l[i][j]==1:
                    c+=1
            
            c1.append(c)
        
        tmp.append(c1)

        c1=[]
        for i in range(len(l)):
            c=0
            for j in range(len(l)):
                if l[j][i]==1:
                    c+=1
            c1.append(c)
        tmp.append(c1)

        return tmp
        
    def largestOverlapCount(self,l1,l2):
        c=0
        for i in range(len(l1)):
            for j in range(len(l1)):
                if l1[i][j]==l2[i][j]==1:
                    c+=1
        return c
        
        
    def  rotate(self,l,i):
        #Stands for rotation types
        if i==1:
            #shift up
            # tmp=[]
            tmp=l[0]
            # print(tmp)
            
            l.append(tmp)
            l.pop(0)
            print(l)
            # tmp=rc[0][0]
            # rc[0].pop(0)
            # rc.append(tmp)
        elif i==2:
            #shift down
            tmp=l[-1]
            l.insert(0,tmp)
            l.pop()
            tmp=rc[0][-1]
            rc[0].pop()
            rc[0].insert(0,tmp)
        elif i==3:
            #right
            for k in range(len(l)):
                tmp=l[k][-1]
                l[k].insert(0,tmp)
                l[k].pop()
            tmp=rc[1][-1]
            rc[1].pop()
            rc[1].insert(0,tmp)
                
                # print(tmp)
        elif i==4:
            #left
            # print(l)
            for k in range(len(l)):
                tmp=l[k][0]
                l[k].append(tmp)
                l[k].pop(0)
            # tmp=rc[1][0]
            # rc[1].pop(0)
            # rc[1].append(tmp)
            
            
                
            
            
        # print(l)
        return l
            
    def getDifference(self,arr1,arr2):
        s=0

        for i in range(len(arr1)):
            s+=abs(arr1[i]-arr2[i])

        return s

    def getIntervals(self,rc1,rc2):
        # print(rc1,rc2)
        minimum=float("inf")
        idx=0
        minimum=self.getDifference(rc1,rc2)
        for i in range(1,len(rc1)):
            tmp=rc1[0]
            rc1.append(tmp)
            rc1.pop(0)
            tmp=self.getDifference(rc1,rc2)
            if tmp<minimum:
                minimum=tmp
                idx=i
        return idx

    def largestOverlap(self, A, B):
        result=0
        onesina=0
        onesinb=0
        onesina=self.calculateOnes(A)
        onesinb=self.calculateOnes(B)
        rc_a=self.calculateOnesRowColumn(A)
        rc_b=self.calculateOnesRowColumn(B)

        # target=onesinb
        # if onesina<onesinb:
        #     target=onesina

        rowShift=self.getIntervals(rc_a[0],rc_b[0])
        columnShift=self.getIntervals(rc_a[1],rc_b[1])

        # print(rowShift,columnShift)
        tmp_a=A.copy()
        # print("Prinnting")
        # print(A,B)
        # print("Prinnting")
        for i in range(rowShift):
            tmp_a=self.rotate(tmp_a,1)
            print(tmp_a)
        # tmp_b=A.copy()
        for i in range(columnShift):
            tmp_a=self.rotate(tmp_a,4)

        count=self.largestOverlapCount(tmp_a,B)
        # print(tmp_a,B)
        print(count)
        
   
s=Solution()
A = [[1,0],[0,0]]
B=[[0,1],[1,0]]
B = [[0,0,0],
    [0,1,1],
    [0,0,1]]

s.largestOverlap(A,B)

            
        
        
        
        
            
        
        
        