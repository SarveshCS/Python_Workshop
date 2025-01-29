def merge_dictionaries(dict1, dict2):
    # Merging using the update method
    merged_dict = dict1.copy()  # Create a copy of dict1
    merged_dict.update(dict2)    # Update with dict2
    return merged_dict

def merge_dictionaries_operator(dict1, dict2):
    # Merging using the merge operator (Python 3.9+)
    merged_dict = dict1 | dict2
    return merged_dict

if __name__ == "__main__":
    dict_a = {'a': 1, 'b': 2}
    dict_b = {'b': 3, 'c': 4}

    # Merging using the update method
    merged_using_update = merge_dictionaries(dict_a, dict_b)
    print("Merged using update:", merged_using_update)

    # Merging using the merge operator
    merged_using_operator = merge_dictionaries_operator(dict_a, dict_b)
    print("Merged using merge operator:", merged_using_operator)