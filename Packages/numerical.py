# prime number 

def isprime(m):
    count=0
    for i in range(1,m+1):
            if m%i==0:
                count+=1
    if count==2:
        return True
    else:
        return False
    
    
  # Function to generate all Perfect numbers in a given range

def isperfect1(n):
    s=0
    for i in range(1,n//2+1):
        if(n%i==0):
            s=s+i
    return s

def perfectrange(lb,ub):
    for i in range(lb,ub+1):
        if isperfect1(i)==i:
            print(i,end=" ")
    return
perfectrange(1,1500)