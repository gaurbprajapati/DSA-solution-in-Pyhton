

def bubble_sot(arr):
    a=1
    while(a<len(arr)):
        for i  in range (0,len(arr)-a):
            if arr[i]>arr[i+1]:
                temp=arr[i+1]
                arr[i+1]=arr[i]
                arr[i]=temp
        a+=1
        # return arr
a=[2,4,6,1,0,9]
print(a)
bubble_sot(a)
print(a)