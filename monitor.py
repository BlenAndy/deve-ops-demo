# monitor.py
import time
import statistics
from calculator import add, multiply, power

def monitor_performance():
    results = {}
    
    for func_name, func, test_cases in [
        ('Add', add, [(5, 3), (100, 200), (-50, 25)]),
        ('Multiply', multiply, [(5, 3), (100, 200), (-50, 25)]),
        ('Power', power, [(2, 10), (3, 8), (5, 5)])
    ]:
        times = []
        for a, b in test_cases:
            start = time.perf_counter()
            for _ in range(10000):
                func(a, b)
            end = time.perf_counter()
            times.append(end - start)
        
        results[func_name] = {
            'mean': statistics.mean(times),
            'median': statistics.median(times),
            'min': min(times),
            'max': max(times)
        }
    
    return results