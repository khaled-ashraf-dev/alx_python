def fibonacci_sequence(n):
    start = [0, 1]
    
    if n <= 0:
        return []
    
    if n > 0 and n < 3:
        return start[:n]
    
    for i in range(n - 2):
        start.append(start[-1] + start[-2])
    
    return start