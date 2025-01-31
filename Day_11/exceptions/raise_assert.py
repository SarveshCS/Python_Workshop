def validate_positive_number(value):
    if value < 0:
        raise ValueError("Value must be a positive number.")

def check_non_empty_string(value):
    if not value:
        raise ValueError("String cannot be empty.")

def custom_exception_example(value):
    if value < 10:
        raise Exception("Value is too low, must be at least 10.")

def assert_example(value):
    assert value > 0, "Value must be greater than zero."

# Example usage
if __name__ == "__main__":
    try:
        validate_positive_number(-5)
    except ValueError as e:
        print(f"Validation Error: {e}")

    try:
        check_non_empty_string("")
    except ValueError as e:
        print(f"Validation Error: {e}")

    try:
        custom_exception_example(5)
    except Exception as e:
        print(f"Custom Exception: {e}")

    try:
        assert_example(-1)
    except AssertionError as e:
        print(f"Assertion Error: {e}")