# Example of a nested dictionary
nested_dict = {
    'person1': {
        'name': 'John',
        'age': 30,
        'address': {
            'street': '123 Main St',
            'city': 'New York',
            'state': 'NY'
        }
    },
    'person2': {
        'name': 'Jane',
        'age': 25,
        'address': {
            'street': '456 Maple Ave',
            'city': 'Los Angeles',
            'state': 'CA'
        }
    }
}

# Accessing nested dictionary values
print(nested_dict['person1']['name'])  # Output: John
print(nested_dict['person2']['address']['city'])  # Output: Los Angeles

# Adding a new entry to a nested dictionary
nested_dict['person3'] = {
    'name': 'Alice',
    'age': 28,
    'address': {
        'street': '789 Oak Dr',
        'city': 'Chicago',
        'state': 'IL'
    }
}
print(nested_dict['person3'])  # Output: {'name': 'Alice', 'age': 28, 'address': {'street': '789 Oak Dr', 'city': 'Chicago', 'state': 'IL'}}

# Updating a nested dictionary value
nested_dict['person1']['age'] = 31
print(nested_dict['person1']['age'])  # Output: 31

# Deleting a nested dictionary entry
del nested_dict['person2']['address']['state']
print(nested_dict['person2']['address'])  # Output: {'street': '456 Maple Ave', 'city': 'Los Angeles'}