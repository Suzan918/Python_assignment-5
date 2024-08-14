# file_handling_assignment.py

def create_and_write_file():
    try:
        # Create and write to the file
        with open('my_file.txt', 'w') as file:
            file.write("Hello, this is the first line.\n")
            file.write("Here is the second line with a number: 42\n")
            file.write("This is the third line with more text.\n")
        print("File created and written successfully.")
    except (PermissionError, IOError) as e:
        print(f"Error occurred while creating/writing the file: {e}")
    finally:
        print("File creation and writing process completed.")

def read_file():
    try:
        # Read from the file
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while reading the file: {e}")
    finally:
        print("File reading process completed.")

def append_to_file():
    try:
        # Append to the file
        with open('my_file.txt', 'a') as file:
            file.write("Appending the fourth line.\n")
            file.write("Here is the fifth line of appended text.\n")
            file.write("And this is the sixth line added to the file.\n")
        print("Content appended successfully.")
    except (PermissionError, IOError) as e:
        print(f"Error occurred while appending to the file: {e}")
    finally:
        print("File appending process completed.")

def main():
    create_and_write_file()
    read_file()
    append_to_file()
    read_file()  # Read file again to show appended content

if __name__ == "__main__":
    main()
