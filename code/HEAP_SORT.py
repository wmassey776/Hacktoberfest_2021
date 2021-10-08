# USing heapify method.
def heapify(arr, n, i):
   largest = i # largest value
   l = 2 * i + 1 # left child
   r = 2 * i + 2 # right child
   # if left child exists and it greater than root element.
   if l < n and arr[i] < arr[l]:
      largest = l
   # if right child exits it greater than largest element.
   if r < n and arr[largest] < arr[r]:
      largest = r
   # root
   if largest != i:
      arr[i],arr[largest] = arr[largest],arr[i] # swap
      # root.
      heapify(arr, n, largest)
# sort
def heapSort(arr):
   n = len(arr)
# creating a max-heap
   for i in range(n, -1, -1):
      heapify(arr, n, i)
# element extraction
   for i in range(n-1, 0, -1):
# swaping 
      arr[i], arr[0] = arr[0], arr[i] 
      heapify(arr, i, 0)
# main
arr = [2,5,3,8,6,5,4,7]

heapSort(arr)

n = len(arr)

print ("Sorted array is")

for i in range(n):

   print (arr[i],end=" ")
