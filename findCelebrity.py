# Time: O(n)
# Space:O(n) for indegrees array 
# Leetcode: Yes
# Issues: Taking too long in python





# O(n) soln 834 ms
class Solution:
    def findCelebrity(self, n: int) -> int:
        celeb = 0

        for i in range(1,n):
            if knows(celeb,i):
                celeb = i
        
        for i in range(n):
            if i!= celeb and knows(celeb,i) or not knows(i, celeb):
                return -1

        return celeb


# O(n^2) solution Time limit exceeded 

class Solution:
    def findCelebrity(self, n: int) -> int:
        indegrees = [0]* n

        for i in range(n):
            for j in range(i+1,n):
                if i == j:
                    continue
                if knows(i,j):
                    indegrees[i] -=1
                    indegrees[j] +=1
                
                if knows(j,i):
                    indegrees[i] +=1
                    indegrees[j] -=1

                    
        for i in range(n):
            if indegrees[i] == n-1:
                return i
        
        return -1

#  O(n^2) solution Time limit exceeded 

class Solution:
    def findCelebrity(self, n: int) -> int:
        indegrees = [0]* n

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if knows(i,j):
                    indegrees[i] -=1
                    indegrees[j] +=1
                
            
        for i in range(n):
            if indegrees[i] == n-1:
                return i
        
        return -1


