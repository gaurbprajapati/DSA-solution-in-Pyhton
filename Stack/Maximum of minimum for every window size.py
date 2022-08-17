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
            
        ans = [0] * (n + 1)
        for i in range(n + 1):
            ans[i] = 0
            
        for i in range(n):
            Len = ans1[i] - ans2[i] - 1
            ans[Len] = max(ans[Len], arr[i])
        for i in range(n - 1, 0, -1):
            ans[i] = max(ans[i], ans[i + 1])
        ans.pop(0)
        return ans