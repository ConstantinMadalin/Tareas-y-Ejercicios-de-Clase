def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a  
        a, b = b, a + b  
n = 10  
print(f"Los primeros {n} números de Fibonacci son:")
for num in fibonacci(n):
    print(num)