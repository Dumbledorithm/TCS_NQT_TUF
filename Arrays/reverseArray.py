def reverseArrayInPlace(arr):
    begin=0
    end = len(arr) - 1
    while begin<end:
        arr[begin],arr[end] = arr[end],arr[begin]
        begin+=1
        end-=1
    
    return arr

if __name__=="__main__":
    arr1=[1,2,3,4,5]
    print(f"The reversed array is{reverseArrayInPlace(arr1)}")