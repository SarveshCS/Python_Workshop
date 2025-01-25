# function_with_default_arguments.py
def describe_person(name, age=30, city="New York"):
    print(f"{name} is {age} years old and lives in {city}.")

# Using default arguments
describe_person("Alice")
describe_person("Bob", 25)
describe_person("Charlie", city="Los Angeles")