class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        n=len(arr)
        def right(arr):
            n=len(arr)
            stack =[]
            ans = []
            index=n
            for i in range (n-1,-1,-1):
                if len(stack)==0:
                    ans.append(index)
                elif len(stack)>0 and stack[-1][0] < arr[i]:
                    ans.append(stack[-1][1])
                elif len(stack)>0 and stack[-1][0] >= arr[i]:
                    
                    while (len(stack) !=0 and stack[-1][0] >= arr[i]):
                        stack.pop()
                    
                    if len(stack)==0:
                        ans.append(index)
                    else:
                        ans.append(stack[-1][1])
                stack.append([arr[i],i])
            return ans[::-1]
        
        def left(arr):
            n=len(arr)
            stack =[]
            ans = []
            
            for i in range (0,n):
                if len(stack)==0:
                    ans.append(-1)
                elif len(stack)>0 and stack[-1][0] < arr[i]:
                    ans.append(stack[-1][1])
                elif len(stack)>0 and stack[-1][0] >= arr[i]:
                    
                    while (len(stack) !=0 and stack[-1][0] >= arr[i]):
                        stack.pop()
                    
                    if len(stack)==0:
                        ans.append(-1)
                    else:
                        ans.append(stack[-1][1])
                stack.append([arr[i],i])
            return ans
        Left= left(arr)
        Right= right(arr)
        width=[]
        area=[]
        for i in range (n):
            width.append(Right[i]-Left[i]-1)
            area.append(width[i]*arr[i])
        return max(area)