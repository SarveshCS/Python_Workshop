# function_with_variable_length_arguments.py
def describe_person(name, *attributes):
    print(f"{name} has the following attributes:")
    for attribute in attributes:
        print(f"- {attribute}")

# Using variable-length arguments
describe_person("Alice", "smart", "kind", "brave")
describe_person("Bob", "strong", "funny")