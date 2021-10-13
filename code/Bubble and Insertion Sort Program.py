#Bubble sort function
def bubbleSort(arr):
      n = len(arr)
      for i in range(n):
            for j in range(0, n-i-1):
                  if arr[j] > arr[j+1] :
                        arr[j], arr[j+1] = arr[j+1], arr[j]

#Insertion sort function

def insertionSort(arr):
      for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >=0 and key < arr[j] :
                  arr[j+1] = arr[j]
                  j -= 1
            arr[j+1] = key 
               
while True:
      #Menu Driven Program
      print("  Main Menu  ")
      print()
      print("1.Bubble sort")
      print("2.Insertion sort")
      print("3. Exit")
      print()
      opt=int(input("Enter your option: "))
      print()            
      if opt==1:
            arr=[]
            x=int(input("Enter number of numbers: "))
            print()
            for a in range(x):
                  b=int(input("Enter element: "))
                  arr.append(b)
            bubbleSort(arr)
            print()                 
            print ("Sorted array is:")
            for i in range(len(arr)):
                  print ("%d" %arr[i],end="  ")
            print()
            print()

      elif opt==2:
            arr=[]
            x=int(input("Enter number of numbers:"))
            for a in range(x):
                  b=int(input("Enter element: "))
                  arr.append(b)  
            insertionSort(arr)
            print()
            print("Sorted array is:") 
            for i in range(len(arr)):
                  print ("%d" %arr[i],end = "  ")
            print()
            print()
            
      elif opt==3:
            break


