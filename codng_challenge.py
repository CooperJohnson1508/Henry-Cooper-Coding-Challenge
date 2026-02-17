import time
start_time = time.time()

def find_gcf(num1, num2):
    while num2 != 0:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder
    return num1

def is_relatively_prime(a, b):
    if find_gcf(a, b) == 1:
        return True

def totient_maximum(interval):
    print("Calculating")
    m = 0
    for i in range(2, interval+1):
        x = 1
        y = 0
        while x != i:
            if is_relatively_prime(i, x):
                y+=1
            x+=1
        z = i/y
        if z>m:
            m = z
         print(i)
    return m

print(totient_maximum(10000))
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Program Run-Time: {elapsed_time:.6f} seconds")
