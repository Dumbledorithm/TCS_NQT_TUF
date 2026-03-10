def isPrime(num):
    count=0
    for i in range(1,int(num**0.5)+1):
        if(num%i==0):
            count+=1
        
        if(num%i!=i):
            count+=1

    return count==2


if __name__=="__main__":
    number = 23253
    result=isPrime(number)
    print(result)