# calculator.py (Final Merged Version)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    result = round(a / b, 2)
    return f"Result: {result}"

if __name__ == "__main__":
    print("Simple Calculator v1.1")
    print("10 / 3 ->", divide(10, 3))
    print("10 / 0 ->", divide(10, 0))
