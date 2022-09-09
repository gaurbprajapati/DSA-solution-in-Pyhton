


# def insertion_sort(array,n):
#     for i in range (1,len(array)):
#         k=array[i]
#         j=i-1
#         while j>=1 and k<array[j]:
#             array[j+1]=array[j]
#             j=j-1
#         array[j+1]=k
#     return array
# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):
    
	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
        # print(arr) 
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key
        # return arr
        
  


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
	# print ("% d" % arr[i])
    print(arr[i],end=" ")

# This code is contributed by Mohit Kumra


# arr=[6,1,8,99,0,7]
# print(insertionSort(arr))
    
    