





# def bubbel_sort(arr):
#     n=len(arr)
#     a=1
#     while(a<n-1):
#         for i in range (0,n-a):
#             if arr[i]>arr[i+1]:
#                 tem=arr[i]
#                 arr[i]=arr[i+1]
#                 arr[i+1]=tem 
#         a=a-1
#     return arr

def bubble_sort(arr):
  
  a=1
  while(a<len(arr)-1):
    for i in range (0,len(arr)-a):
      if arr[i]>arr[i+1]:
        tem=arr[i]
        arr[i]=arr[i+1]
        arr[i+1]=tem    
    a=a+1
  # for item in arr:
  #   print(item)
  return arr
        
a=[3,2,5,7,0,5976,1,7,30,1,2,36,4,78,6]
print(bubble_sort(a))