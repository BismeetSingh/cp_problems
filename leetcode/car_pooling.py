#https://leetcode.com/problems/car-pooling/
#Sort by start and end times and store end times and capacity on the min heap.
#Nlogn
#Compare start times with minim values on the heap and if at any time the capacity is less than 0 then return False.
from heapq import *
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key=lambda x:(x[1],x[2]))
        i=0
        heap=[]
        while i<len(trips):
            trip=trips[i]
            capacity-=trip[0]
            # print("Capacity",capacity)
            if len(heap)==0:
                to_push=(trip[2],trip[0])
                heappush(heap,to_push)
            else:
                while len(heap)>0 and trip[1]>=heap[0][0]:
                    capacity+=heap[0][1]
                    heappop(heap)
                to_push=(trip[2],trip[0])
                heappush(heap,to_push)
            if capacity<0:
                return False
            i+=1
        return capacity>=0
                    
                    
                    
                    
                    
        