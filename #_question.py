def create_and_write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Content written to {filename} successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
                
# Example usage
filename = 'example.txt'
content = "This is some example content."
create_and_write_file(filename, content)