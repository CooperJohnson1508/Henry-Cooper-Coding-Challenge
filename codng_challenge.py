import time
start_time = time.time()

def euler_totient(n):
    """Calculate Euler's totient using prime factorization - O(sqrt(n))"""
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def totient_maximum(interval):
    m = 0
    best_i = 0
    for i in range(2, interval+1):
        phi = euler_totient(i)
        z = i / phi
        if z > m:
            m = z
            best_i = i
    return best_i

print(totient_maximum(1000))
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Program Run-Time: {elapsed_time:.6f} seconds")

#they
