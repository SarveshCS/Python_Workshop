def optimize_memory():
    # Using tuples for memory efficiency
    tuple_data = (1, 2, 3, 4, 5)
    print("Tuple:", tuple_data)
    print("Memory size of tuple:", tuple_data.__sizeof__(), "bytes")

    # Using lists for comparison
    list_data = [1, 2, 3, 4, 5]
    print("List:", list_data)
    print("Memory size of list:", list_data.__sizeof__(), "bytes")

    # Demonstrating the use of frozenset for memory optimization
    frozenset_data = frozenset([1, 2, 3, 4, 5])
    print("Frozenset:", frozenset_data)
    print("Memory size of frozenset:", frozenset_data.__sizeof__(), "bytes")

if __name__ == "__main__":
    optimize_memory()