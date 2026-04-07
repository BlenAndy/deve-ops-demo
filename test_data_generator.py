# test_data_generator.py
import random
from calculator import add, subtract, multiply, divide, power

def generate_test_data(num_cases=100):
    """Generate random test cases"""
    test_results = []
    for _ in range(num_cases):
        a = random.randint(-100, 100)
        b = random.randint(-100, 100)
        
        test_results.append({
            'add': add(a, b),
            'subtract': subtract(a, b),
            'multiply': multiply(a, b),
            'power': power(a, abs(b) % 5)  # Limit exponent
        })
    
    print(f"✅ Generated {num_cases} test cases")
    return test_results