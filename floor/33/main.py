from math import sqrt


def prime(n):
    if n<=3:
        return n>=2
    if (n+1)%6!=0 and (n-1)%6!=0:
        return False
    for i in range(2,int(sqrt(n)+1)):
        if n%i==0:
            return False
    return True

if __name__ == '__main__':
    s=0
    for i in range(2,101):
        if prime(i):
            s+=i
    print(s)
    
    n=int(input())
    print(isPrime(n))
