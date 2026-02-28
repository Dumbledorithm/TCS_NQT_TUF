def findSecondSmallest(arr,n):
    secondSmallest = float('inf')
    smallest = float('inf')
    for i in range(0,n):
        if arr[i] < smallest:
            secondSmallest = smallest
            smallest = arr[i]
        elif smallest<arr[i]<secondSmallest:
            secondSmallest=arr[i]

    if secondSmallest == float('inf'):
        return -1
        
    return secondSmallest

def findSecondLargest(arr,n):
    largest=float('-inf')
    secondLargest = float('-inf')

    for i in range(0,n):
        if arr[i]>largest:
            secondLargest = largest
            largest=arr[i]
        
        elif secondLargest<arr[i]<largest:
            secondLargest = arr[i]

    if secondLargest == float('-inf'):
        return -1
    
    return secondLargest

if __name__=="__main__":
    arr1=[1,2,3,2,5,6,1]
    n=len(arr1)

    print(f"The second smallest element in the array is: {findSecondSmallest(arr1,n)}")
    print(f"The second largest element in the array is: {findSecondLargest(arr1,n)}")