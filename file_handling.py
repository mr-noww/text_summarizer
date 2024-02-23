
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Content has been successfully written to '{filename}'.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
# Read from a file
# file_content = read_file("example.txt")
# if file_content:
#     print("File content:")
#     print(file_content)
