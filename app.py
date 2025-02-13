# app.py
def add(a: int, b: int) -> int:
    """Returns the sum of two numbers."""
    return a + b

def multiply(a: int, b: int) -> int:
    """Returns the product of two numbers."""
    return a * b

if __name__ == "__main__":
    print("Addition:", add(2, 3))
    print("Multiplication:", multiply(2, 3))

