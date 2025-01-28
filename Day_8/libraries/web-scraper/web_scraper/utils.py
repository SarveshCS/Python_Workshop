def clean_text(text):
    """Cleans the input text by removing unnecessary whitespace and special characters."""
    return ' '.join(text.split())

def save_to_file(data, filename):
    """Saves the given data to a specified file."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)