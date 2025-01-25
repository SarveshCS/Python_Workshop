# function_with_variable_length_keyword_arguments.py
def describe_person(name, **attributes):
    print(f"{name} has the following attributes:")
    for key, value in attributes.items():
        print(f"- {key}: {value}")

# Using variable-length keyword arguments
describe_person("Alice", age=30, city="New York", profession="Engineer")
describe_person("Bob", age=25, city="Los Angeles", hobby="Photography")