class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,arr,n):
        s=[]
        ans= []
        
        for i in range (0,n):
            
            
            if len(s)==0:
                ans.append(-1)
            elif (len(s)>0 and s[-1][0]>arr[i]):
                ans.append(s[-1][1])
            elif (len(s)>0 and s[-1][0]<arr[i]):
                while (len(s)!=0 and s[-1][0]<arr[i]):
                    s.pop()
                if len(s)==0:
                    ans.append(-1)
                else:
                    ans.append(s[-1][1])
            s.append([arr[i],i])
        
        
        for i in range (n):
            ans[i]=i-ans[i]
        return ans