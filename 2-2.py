'''
n!=1 * 2 * 3 * ⋯ * n
'''

def fact_array(n):
    if n < 0:
        return "Invalid input!"
    
    numbers = [i for i in range(1, n + 1)]
    
    fact = 1
    for num in numbers:
        fact *= num
    
    return fact


n = int(input("Enter a positive integer: "))
result = fact_array(n)
print(f"The fact of {n} is: {result}")

