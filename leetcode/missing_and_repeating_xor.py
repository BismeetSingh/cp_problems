
def repeatedNumber(A): 
      
    length = len(A) 
    Sum_N = (length * (length + 1)) // 2
    Sum_NSq = ((length * (length + 1) * 
                     (2 * length + 1)) // 6) 
      
    missingNumber, repeating = 0, 0
    # print(Sum_N,Sum_NSq)
    for i in range(len(A)): 
        Sum_N -= A[i] 
        Sum_NSq -= A[i] * A[i] 
    print(Sum_N,Sum_NSq)
    #Sumn is (x-y) and sumnsq is (x^2-y^2)
    missingNumber = (Sum_N + Sum_NSq // Sum_N) // 2
    repeating = missingNumber - Sum_N 
      
    ans = [] 
    ans.append(repeating) 
    ans.append(missingNumber) 
      
    return ans 
  
# Driver code 
v = [ 4, 3, 6, 2, 1,1] 
res = repeatedNumber(v) 
  
for i in res: 
    print(i, end = " ") 

# arr=[4,3,6,2,1,1]
# missing_and_repeating_xor(arr)