l=[int(x) for x in input().split()]
n=len(l)
x=int(input())
def binary_search(l,x):
    low=0
    mid=0
    high=len(l)-1
    step=0
    while(low<=high):
        mid=(high+low)//2
        if(l[mid]<x):
            low=mid+1
        elif(l[mid]>x):
            high=mid-1
        else:
            return mid
    return -1
result=binary_search(l,x)
if(result!=-1):
    print(x,"is found at the position",str(result))
else:
    print("ELEMENT IS NOT PRESENT IN ARRAY")
