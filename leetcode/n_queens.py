# class Solution:.

def isSafe(row,col,board,n):
    for i in range(0,row):
        # print("State",i,col)
        if board[i][col]==1:
            return False
    #Check top left diagonal
    i=row
    j=col
    while(i>=0 and j>=0):
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    #Check top right diagonal   
    i=row
    j=col
    while(i>=0 and j<n):
        if board[i][j]==1:
            return False
        j+=1
        i-=1
    return True
    
    
def place_queen(row,board,n):
    global count
    if row>=n:
        count+=1
        for i in range(n):
            for j in range(n):
                if board[i][j]==1:
                    print("Q",end=" ")
                else:
                    print(board[i][j],end=" ")
            print()
        print()
        #Changing return true to false makes false bubble up and then it starts searching again bt since we counted the combination already ,we are okay.
        return False
    for i in range(n):
        if(isSafe(row,i,board,n)):
            board[row][i]=1
            #If we place current Queen, we check whether next row can place a queen ,if it cant,False gets bubbled upwards until we backtrack.
            if place_queen(row+1,board,n):
                return True
            board[row][i]="X"
    return False
    
count=0
def totalNQueens(n):  
    board=[["X"]*(n) for i in range(n)]
    
    place_queen(0,board,n)
    return count
    
print(totalNQueens(5))