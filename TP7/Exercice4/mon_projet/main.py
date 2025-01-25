# main.py

from src.math_operations import add, subtract, multiply, divide
from src.string_operations import concatenate, to_uppercase

def main():
    print("Addition: ", add(5, 3))
    print("Subtraction: ", subtract(10, 4))
    print("Multiplication: ", multiply(6, 7))
    print("Division: ", divide(8, 2))

    print("Concatenate: ", concatenate("Hello, ", "World!"))
    print("Uppercase: ", to_uppercase("hello"))

if __name__ == "__main__":
    main()
