
from math import floor,sqrt
def simpleSieve(limit, primes):
    mark = [False]*(limit+1)
 
    for i in range(2, limit+1):
        if not mark[i]:
 
            # If not marked yet,
            # then its a prime
            primes.append(i)
            for j in range(i, limit+1, i):
                mark[j] = True
 
 
# Finds all prime numbers
# in given range using
# segmented sieve
def primesInRange(low, high):
 
    # Comput all primes smaller
    # or equal to
    # square root of high
    # using simple sieve
    limit = floor(sqrt(high)) + 1
    primes = list()
    simpleSieve(limit, primes)
     
    if low < 2:
      low=2
    #Neglecting 0 or 1 value of low
 
    # Count of elements in given range
    n = high - low + 1
 
    # Declaring boolean only for
    # [low, high]
    mark = [False]*(n+1)
 
    # Use the found primes by
    # simpleSieve() to find
    # primes in given range
    for i in range(len(primes)):
 
        # Find the minimum number
        # in [low..high] that is
        # a multiple of prime[i]
        # (divisible by prime[i])
        loLim = floor(low/primes[i]) * primes[i]
        if loLim < low:
            loLim += primes[i]
        if loLim == primes[i]:
            loLim += primes[i]
 
        # Mark multiples of primes[i]
        # in [low..high]:
        # We are marking j - low for j,
        # i.e. each number
        # in range [low, high] is mapped
        # to [0, high-low]
        # so if range is [50, 100]
        # marking 50 corresponds
        # to marking 0, marking 51
        # corresponds to 1 and
        # so on. In this way we need
        # to allocate space
        # only for range
        for j in range(loLim, high+1, primes[i]):
            mark[j-low] = True
 
    # Numbers which are not marked
    # in range, are prime
    cnt=0
    for i in range(low, high+1):
        if not mark[i-low]:
            cnt+=1
    return cnt
 

for _ in range(int(input())):
    n=int(input())
    if n==2:
        print(1)
        continue
    if n==3:
        print(2)
        continue
    if n==4:
        print(2)
        continue
    if n==5:
        print(3)
        continue
    if n==6:
        print(2)
        continue
    else:
        cnt=primesInRange(n//2+1,n)
        print(1+cnt)
