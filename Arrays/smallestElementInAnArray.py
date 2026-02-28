def sortArr(arr):
    arr.sort()
    return arr[0]

if __name__ == "__main__":
    arr1 = [1,2,3,4,5,6]
    print(f"The smallest element in the array is:{sortArr(arr1)}")