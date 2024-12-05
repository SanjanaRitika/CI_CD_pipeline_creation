from main import calculate_factorial

def test_calculate_factorial():
    assert calculate_factorial(5) == 120
    assert calculate_factorial(0) == 1
    assert calculate_factorial(1) == 1
    assert calculate_factorial(-4) == "Invalid Input"
    assert calculate_factorial("string") == "Invalid Input"
