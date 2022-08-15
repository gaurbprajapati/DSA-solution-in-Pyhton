
class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        ans = -1
        for i in range (n):
            
            if 1 in M[i]:
                pass
            else:
                ans=i
        
        if ans == -1:
            return -1
        if ans+1 == n:
            for  i in range (ans-1, -1 , -1):
                if 1 not in M[i]:
                    return -1
                else:
                    pass
        for j in range (ans, n):
            if 1 in M[i]:
                pass
            else:
                return -1
        
        return ans