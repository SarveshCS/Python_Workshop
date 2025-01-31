import os

def create_directory(dir_name):
    try:
        os.makedirs(dir_name, exist_ok=True)
        print(f"Directory '{dir_name}' created successfully.")
    except Exception as e:
        print(f"Error creating directory '{dir_name}': {e}")

def list_directories(parent_dir):
    try:
        with os.scandir(parent_dir) as entries:
            print(f"Directories in '{parent_dir}':")
            for entry in entries:
                if entry.is_dir():
                    print(f" - {entry.name}")
    except Exception as e:
        print(f"Error listing directories in '{parent_dir}': {e}")