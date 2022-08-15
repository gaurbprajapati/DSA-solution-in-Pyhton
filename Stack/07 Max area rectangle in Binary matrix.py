class Solution:
    def maximalRectangle(self, arr: List[List[str]]) -> int:
        n=len(arr)
        m=len(arr[0])
        def mah(arr):
            n=len(arr)
            stack =[]
            ans1 = []
            index=n
            for i in range (n-1,-1,-1):
                if len(stack)==0:
                    ans1.append(index)
                elif len(stack)>0 and stack[-1][0] < arr[i]:
                    ans1.append(stack[-1][1])
                elif len(stack)>0 and stack[-1][0] >= arr[i]:
                    while (len(stack) !=0 and stack[-1][0] >= arr[i]):
                        stack.pop()
                    
                    if len(stack)==0:
                        ans1.append(index)
                    else:
                        ans1.append(stack[-1][1])
                stack.append([arr[i],i])
            ans1= ans1[::-1]
            stack =[]
            ans2 = []
            
            for i in range (0,n):
                if len(stack)==0:
                    ans2.append(-1)
                elif len(stack)>0 and stack[-1][0] < arr[i]:
                    ans2.append(stack[-1][1])
                elif len(stack)>0 and stack[-1][0] >= arr[i]:
                    while (len(stack) !=0 and stack[-1][0] >= arr[i]):
                        stack.pop()
                    if len(stack)==0:
                        ans2.append(-1)
                    else:
                        ans2.append(stack[-1][1])
                stack.append([arr[i],i])
            ans  = -100000000000
            for i in range (n):
                ans = max(ans,((ans1[i]-ans2[i]-1)*arr[i]))
            return ans    
        
        v=[]
        for  i in range (m):
            v.append(int(arr[0][i]))
        mx = mah(v)
        for i in range (1,n):
            for j in range (m):
                if arr[i][j]=='0':
                    v[j]=0
                else:
                    v[j]=v[j]+int(arr[i][j])
            mx = max(mx,mah(v))
        return mx