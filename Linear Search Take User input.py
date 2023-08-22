print("Linear Search using define function:")
arr=[]
size=int(input('Please Enter Your Size Of Array: '))
print("Please Enter Your Value for array:")
for i in range(size):
    b=int(input())
    arr.append(b)
print(arr)

len_arr=len(arr)
def LinearSearch():
    searchValue=int(input('Please Enter Your your Number which you want to search: '))
    for i in range(len_arr):
        if (arr[i]==searchValue):
            return i
    return -1
    
result=LinearSearch()

#print("Your Value IS:",result)
if result==-1:
    print("Element Not Found")
else:
    print("Your Enlent on index: ",result)

    
print("Binary Search using define function:")

def BinarySearch():
    target=int(input("Please Inter Your Element for Search: "))
    low= 0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<taret:
            low=mid+1
        else:
            high=mid-1
            return -1
result1=BinarySearch()
if result1 ==-1:
    print("Element Not Found")
else:
    print("Elent On Index: ",result1)
