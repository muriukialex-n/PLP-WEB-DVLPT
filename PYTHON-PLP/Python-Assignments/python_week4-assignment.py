# File Handling and Exception Handling Assignment

# Challenge 1: File Read & Write Challenge
def file_read_write_challenge():
    """
    Create a program that reads a file and writes a modified version to a new file.
    """
    try:
        # Get filename from user
        filename = input("Enter the filename to read: ")
        
        # Read the original file
        with open(filename, 'r') as file:
            content = file.read()
        
        print(f"Original content:\n{content}")
        
        # Modify the content (example: convert to uppercase and add line numbers)
        lines = content.split('\n')
        modified_content = ""
        for i, line in enumerate(lines, 1):
            modified_content += f"{i}. {line.upper()}\n"
        
        # Write to a new file
        new_filename = f"modified_{filename}"
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        
        print(f"\nModified content written to '{new_filename}':")
        print(modified_content)
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read/write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Challenge 2: Error Handling Lab
def error_handling_lab():
    """
    Ask the user for a filename and handle errors if it doesn't exist or can't be read.
    """
    while True:
        try:
            filename = input("\nEnter a filename to read (or 'quit' to exit): ")
            
            if filename.lower() == 'quit':
                print("Goodbye!")
                break
            
            # Attempt to open and read the file
            with open(filename, 'r') as file:
                content = file.read()
                print(f"\nFile '{filename}' content:")
                print("-" * 40)
                print(content)
                print("-" * 40)
                
                # Display file statistics
                lines = content.split('\n')
                words = content.split()
                characters = len(content)
                
                print(f"\nFile Statistics:")
                print(f"Lines: {len(lines)}")
                print(f"Words: {len(words)}")
                print(f"Characters: {characters}")
                
        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist.")
            print("Please check the filename and try again.")
            
        except PermissionError:
            print(f"Error: Permission denied to read '{filename}'.")
            print("You don't have the necessary permissions to access this file.")
            
        except IsADirectoryError:
            print(f"Error: '{filename}' is a directory, not a file.")
            
        except UnicodeDecodeError:
            print(f"Error: Cannot decode '{filename}'. It might be a binary file.")
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Additional utility function: Create sample files for testing
def create_sample_files():
    """
    Create sample files for testing the assignment functions.
    """
    try:
        # Create a sample text file
        with open('sample.txt', 'w') as file:
            file.write("""Hello World!
This is a sample file for testing.
It contains multiple lines.
File handling is important in programming.
Python makes it easy with proper exception handling.""")
        
        print("Sample file 'sample.txt' created for testing.")
        
        # Create another sample file
        with open('data.txt', 'w') as file:
            file.write("""Name: John Doe
Age: 25
City: New York
Occupation: Software Developer
Hobby: Reading books""")
        
        print("Sample file 'data.txt' created for testing.")
        
    except Exception as e:
        print(f"Error creating sample files: {e}")

# Main program
def main():
    print("File Handling and Exception Handling Assignment")
    print("=" * 60)
    
    while True:
        print("\nSelect an option:")
        print("1. File Read & Write Challenge")
        print("2. Error Handling Lab")
        print("3. Create Sample Files (for testing)")
        print("4. Exit")
        
        try:
            choice = input("\nEnter your choice (1-4): ")
            
            if choice == '1':
                print("\nFile Read & Write Challenge")
                print("-" * 40)
                file_read_write_challenge()
                
            elif choice == '2':
                print("\nError Handling Lab")
                print("-" * 40)
                error_handling_lab()
                
            elif choice == '3':
                print("\nCreating Sample Files")
                print("-" * 40)
                create_sample_files()
                
            elif choice == '4':
                print("\nThank you for using the File Handling Assignment!")
                break
                
            else:
                print("Invalid choice. Please select 1-4.")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
