# Created this file with the file tool
# Just checking whether working properly or not.

def is_even(number):
    """Return True if number is even, False otherwise."""
    return number % 2 == 0

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        if is_even(num):
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")
    except ValueError:
        print("Please enter a valid integer.")