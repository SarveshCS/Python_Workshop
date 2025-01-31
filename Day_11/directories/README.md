# Directory Operations in Python

This document provides an overview of how to work with directories in Python, focusing on creating and listing directories using the `os` module. It also covers exception handling to manage potential errors that may arise during these operations.

## Creating Directories

To create a directory in Python, you can use the `os.makedirs()` function. This function allows you to create a directory recursively, meaning it can create all intermediate-level directories needed to contain the leaf directory.

### Example

```python
import os

def create_directory(dir_name):
    try:
        os.makedirs(dir_name, exist_ok=True)
        print(f"Directory '{dir_name}' created successfully.")
    except Exception as e:
        print(f"Error creating directory '{dir_name}': {e}")
```

### Edge Cases

- **Existing Directory**: If the directory already exists, using `exist_ok=True` prevents an error from being raised.
- **Permissions Error**: If the program does not have permission to create a directory in the specified location, an exception will be raised.

## Listing Directories

To list directories within a parent directory, you can use `os.scandir()`. This function returns an iterator of `os.DirEntry` objects corresponding to the entries in the directory.

### Example

```python
def list_directories(parent_dir):
    try:
        with os.scandir(parent_dir) as entries:
            print(f"Directories in '{parent_dir}':")
            for entry in entries:
                if entry.is_dir():
                    print(entry.name)
    except Exception as e:
        print(f"Error listing directories in '{parent_dir}': {e}")
```

### Edge Cases

- **Non-Existent Parent Directory**: If the specified parent directory does not exist, a `FileNotFoundError` will be raised.
- **Permissions Error**: Similar to creating directories, if the program lacks permission to access the parent directory, an exception will be raised.

## Conclusion

This document serves as a guide for basic directory operations in Python. By understanding how to create and list directories, along with handling exceptions, you can effectively manage directory structures in your applications.