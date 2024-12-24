import os

# File to store youth esports member data
FILE_NAME = "youth_esports_members.txt"

def add_member():
    """Add a new member and save the information to a file."""
    name = input("Enter member's name: ")
    age = input("Enter member's age: ")
    game = input("Enter member's favorite game: ")
    level = input("Enter member's skill level (Beginner/Intermediate/Advanced): ")
    guardian_name = input("Enter guardian's name: ")
    guardian_contact = input("Enter guardian's contact information: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{age},{game},{level},{guardian_name},{guardian_contact}\n")

    print(f"Member {name} added successfully!")

def list_members():
    """List all youth esports members from the file."""
    if not os.path.exists(FILE_NAME):
        print("No members found. The file does not exist.")
        return

    with open(FILE_NAME, "r") as file:
        members = file.readlines()

    if not members:
        print("No members found.")
    else:
        print("\nCurrent Members:")
        for idx, member in enumerate(members, 1):
            name, age, game, level, guardian_name, guardian_contact = member.strip().split(",")
            print(f"{idx}. Name: {name}, Age: {age}, Game: {game}, Level: {level}, Guardian: {guardian_name}, Contact: {guardian_contact}")

def delete_member():
    """Delete a member from the file by index."""
    if not os.path.exists(FILE_NAME):
        print("No members found. The file does not exist.")
        return

    with open(FILE_NAME, "r") as file:
        members = file.readlines()

    if not members:
        print("No members to delete.")
        return

    list_members()
    try:
        index = int(input("Enter the number of the member to delete: ")) - 1
        if index < 0 or index >= len(members):
            print("Invalid selection. No member deleted.")
            return

        del members[index]
        with open(FILE_NAME, "w") as file:
            file.writelines(members)

        print("Member deleted successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Example Usage
if __name__ == "__main__":
    while True:
        print("\nYouth Esports Member Management")
        print("1. Add Member")
        print("2. List Members")
        print("3. Delete Member")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            add_member()
        elif choice == "2":
            list_members()
        elif choice == "3":
            delete_member()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
