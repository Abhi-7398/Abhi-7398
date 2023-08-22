Array=[]
size=int(input("Please Enter Your Size Of Array: "))
print("Please Enter The Element OF Array: ")
for i in range(size):
    elem=int(input())
    Array.append(elem)
print("Array is: ",Array)    
def BubbleSort():
    for i in range(len(Array)):
        for j in range(len(Array)-i-1):
            if Array[j]>Array[j+1]:
                temp=Array[j]
                Array[j]=Array[j+1]
                Array[j+1]=temp
BubbleSort()
print("Sorted Array is: ",Array)
