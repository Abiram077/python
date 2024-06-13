def is_prime(x):
    for i in range(2,x):    #starts 2 cuz the python wil take 2 as the starting point even we start from 0
        if x% i == 0:       # if its remainder is  0 not prime num
            return False
    return True

def n_thprime(x):
    num = 3
    prime=2
    if x == 1:
        return 2
    while prime<x:
        num+=2
        while not is_prime(num):
            num+=2
        prime+=1
    return num

prime = list(range(1,100))
for i in prime:
    print(i,n_thprime(i))