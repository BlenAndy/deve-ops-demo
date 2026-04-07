# test_api.py
import requests
import json

def test_api_endpoints():
    """Test calculator API endpoints"""
    base_url = "http://localhost:5000"
    
    # Test health endpoint
    response = requests.get(f"{base_url}/health")
    assert response.status_code == 200
    
    # Test calculation endpoint
    test_cases = [
        ('add', 5, 3, 8),
        ('subtract', 10, 4, 6),
        ('multiply', 6, 7, 42),
        ('divide', 15, 3, 5),
        ('power', 2, 4, 16)
    ]
    
    for op, a, b, expected in test_cases:
        payload = {'operation': op, 'a': a, 'b': b}
        response = requests.post(f"{base_url}/calculate", json=payload)
        assert response.json()['result'] == expected
    
    print("✅ API tests passed")