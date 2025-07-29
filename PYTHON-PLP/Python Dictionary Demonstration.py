# Python Dictionary Demonstration

# 1. Creating a dictionary
student = {
    "name": "Alice",
    "age": 21,
    "course": "Computer Science",
    "grades": [85, 90, 78]
}

print("Original Dictionary:")
print(student)

# 2. Accessing dictionary values
print("\nAccessing Values:")
print("Name:", student["name"])
print("Grades:", student["grades"])

# 3. Modifying dictionary values
student["age"] = 22
print("\nUpdated Age:")
print(student["age"])

# 4. Adding new key-value pairs
student["graduated"] = False
print("\nAdded Graduation Status:")
print(student)

# 5. Removing a key-value pair
del student["course"]
print("\nAfter Removing 'course':")
print(student)

# 6. Checking if a key exists
print("\nCheck if 'name' key exists:")
print("name" in student)

# 7. Iterating through a dictionary
print("\nIterating Through Dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")

# 8. Using dictionary methods
print("\nUsing Dictionary Methods:")
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# 9. Copying a dictionary
student_copy = student.copy()
print("\nCopied Dictionary:")
print(student_copy)

# 10. Clearing a dictionary
student_copy.clear()
print("\nCleared Copy:")
print(student_copy)

# Interactive Python Dictionary Program

def display_menu():
    print("\nDictionary Operations Menu:")
    print("1. Show Dictionary")
    print("2. Access a Value")
    print("3. Add or Update a Key-Value Pair")
    print("4. Delete a Key")
    print("5. Check if a Key Exists")
    print("6. Show All Keys")
    print("7. Show All Values")
    print("8. Show All Items")
    print("9. Clear Dictionary")
    print("0. Exit")

# Initial dictionary
student = {
    "name": "Alice",
    "age": 21,
    "grades": [85, 90, 78]
}

while True:
    display_menu()
    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("Current Dictionary:", student)

    elif choice == "2":
        key = input("Enter the key you want to access: ")
        if key in student:
            print(f"{key} => {student[key]}")
        else:
            print("Key not found!")

    elif choice == "3":
        key = input("Enter the key to add/update: ")
        value = input("Enter the value: ")
        try:
            value = eval(value)  # Convert to correct data type
        except:
            pass
        student[key] = value
        print("Key-value pair updated.")

    elif choice == "4":
        key = input("Enter the key to delete: ")
        if key in student:
            del student[key]
            print("Key deleted.")
        else:
            print("Key not found!")

    elif choice == "5":
        key = input("Enter the key to check: ")
        if key in student:
            print("Key exists.")
        else:
            print("Key does not exist.")

    elif choice == "6":
        print("Keys:", list(student.keys()))

    elif choice == "7":
        print("Values:", list(student.values()))

    elif choice == "8":
        print("Items:", list(student.items()))

    elif choice == "9":
        student.clear()
        print("Dictionary cleared.")

    elif choice == "0":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")