

def prime_numbers(num):
    if num< 2:
        return False
    
    for i in range(2,num):
        if (num%i) == 0:
            return False

    return True
for i in range(0, 100+1):
    if prime_numbers(i):
        print(i, end=' ')