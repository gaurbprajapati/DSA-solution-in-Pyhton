

def mergesort(list1):
    #mid=len(list1)//21
    if len(list1)>1:
        mid =len(list1)//2
        left_lest=list1[:mid]
        right_lest=list1[mid:]
        mergesort(left_lest)
        mergesort(right_lest)
        i=0
        j=0
        k=0
        while i<len(left_lest) and j<len(right_lest):
            if left_lest[i]<right_lest[j]:
                list1[k]=left_lest[i]
                i+=1
                k+=1
            else:
                list1[k]=right_lest[j]
                j=j+1;k=k+1
        while i<len(left_lest):
            list1[k]=left_lest[i]
            i=i+1
            j=j+1
        while j<len(right_lest):
            list1[k]=right_lest[j]
            j=j+1
            k=k+1
            return list1

num=int(input("enter no of element in list:--"))
list = [int(input()) for l in range (num) ]

print("Old array without sorting:--",list)
mergesort(list)
print("New array with sorting accending order:--",list)