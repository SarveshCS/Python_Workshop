# function_with_keyword_arguments.py
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

# Using keyword arguments
describe_person(name="Alice", age=30, city="New York")
describe_person(city="Los Angeles", name="Bob", age=25)