def isPalindrome(number):
    rev = 0
    original = number
    while (number>0):
        lastdigit = number%10
        rev = (rev*10)+lastdigit
        number = number//10
        
    return rev == original
    

#Driver code
if __name__=="__main__":
    starting_number=input("Enter the starting num")
    ending_number=input("ENter the ending num")
    for i in range(starting_number,ending_number+1):
        if isPalindrome(i):
            print(i,end="")
        
    