def fibonacci(n):
    fib_sequence = [0, 1]  
    for _ in range(n - 2): 
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

print(fibonacci(10))
