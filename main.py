import os
import time

# -------------------- Class Definition --------------------

class Member:
    def __init__(self, name, member_id, email, status="inactive"):
        self.name = name
        self.member_id = member_id
        self.email = email
        self.status = status

    def show_all_members(self):
        print("Your name:", self.name)
        print("Your ID:", self.member_id)
        print("Your email:", self.email)
        print("Your status:", self.status)

    def to_line(self):
        return f"{self.name},{self.member_id},{self.email},{self.status}\n"

    @staticmethod
    def from_line(line):
        name, member_id, email, status = line.strip().split(",")
        return Member(name, member_id, email, status)

# -------------------- File Operations --------------------

def save_members_to_file(filename="members.txt"):
    with open(filename, "w") as file:
        for member in all_members:
            file.write(member.to_line())

def load_members_from_file(filename="members.txt"):
    try:
        with open(filename, "r") as file:
            for line in file:
                all_members.append(Member.from_line(line))
    except FileNotFoundError:
        pass

# -------------------- Utility --------------------

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_member():
    name = input("Enter your name: ").lower()
    member_id = input("Enter your ID: ").lower()
    email = input("Enter your email: ").lower()
    status = input("Enter status (active/inactive) or press Enter to skip: ").lower()
    if status not in ["active", "inactive"]:
        status = "inactive"
    return Member(name, member_id, email, status)

# -------------------- Member Actions --------------------

def edit_member(member):
    print("Leave blank if you don’t want to change the field.")
    new_name = input(f"New name [{member.name}]: ").strip().lower()
    new_email = input(f"New email [{member.email}]: ").strip().lower()
    new_status = input(f"New status (active/inactive) [{member.status}]: ").strip().lower()

    if new_name:
        member.name = new_name
    if new_email:
        member.email = new_email
    if new_status in ["active", "inactive"]:
        member.status = new_status

    save_members_to_file()
    print("Member updated successfully.")
    time.sleep(2)

def delete_member(member):
    all_members.remove(member)
    save_members_to_file()
    print("Member deleted successfully.")
    time.sleep(2)

# -------------------- Search Functions --------------------

def search_by_name():
    name_search = input("Enter name: ").lower()
    found = False
    print("*" * 50)
    for member in all_members:
        if member.name.lower() == name_search:
            member.show_all_members()
            print("*" * 50)
            found = True
            time.sleep(1)
    if not found:
        print("Name not found.")
    input("Press Enter to continue...")
    clear_screen()

def search_by_id():
    id_search = input("Enter ID: ")
    found = False
    for member in all_members:
        if member.member_id == id_search:
            print("*" * 50)
            member.show_all_members()
            print("*" * 50)
            found = True

            action = input("Do you want to [E]dit, [D]elete, or [Enter] to skip? ").strip().lower()
            if action == "e":
                edit_member(member)
            elif action == "d":
                delete_member(member)
            else:
                print("No action taken.")
                time.sleep(2)
            break

    if not found:
        print("ID not found.")
        time.sleep(2)

    input("Press Enter to continue...")
    clear_screen()

def search_by_email():
    email_search = input("Enter email: ").lower()
    found = False
    print("*" * 50)
    for member in all_members:
        if member.email == email_search:
            member.show_all_members()
            print("*" * 50)
            found = True
            time.sleep(1)
    if not found:
        print("Email not found.")
    input("Press Enter to continue...")
    clear_screen()

def search_by_status():
    status_search = input("Search by status:\n1: inactive\n2: active\n--> ").lower()
    found = False
    if status_search in ["1", "inactive"]:
        target_status = "inactive"
    elif status_search in ["2", "active"]:
        target_status = "active"
    else:
        print("Invalid input.")
        time.sleep(2)
        clear_screen()
        return

    print("*" * 50)
    for member in all_members:
        if member.status == target_status:
            member.show_all_members()
            print("*" * 50)
            found = True
            time.sleep(1)

    if not found:
        print("No members found with this status.")
    input("Press Enter to continue...")
    clear_screen()

# -------------------- Main Program --------------------

all_members = []
load_members_from_file()

while True:
    print("1: Add user")
    print("2: Show users")
    print("3: Search user")
    print("4: Exit")
    choice = input("Your choice: ").strip()

    if choice == "1":
        print("_" * 50)
        all_members.append(add_member())
        save_members_to_file()
        print("User added successfully.")
        print("Loading...")
        time.sleep(2)
        clear_screen()

    elif choice == "2":
        if all_members:
            for member in all_members:
                print("Loading...")
                time.sleep(1)
                print("*" * 50)
                member.show_all_members()
                print("*" * 50)
            input("Press Enter to continue...")
        else:
            print("No members available.")
            time.sleep(2)
        clear_screen()

    elif choice == "3":
        if all_members:
            print("-" * 50)
            search_choice = input("Search by:\n1: name\n2: ID\n3: email\n4: status\n--> ").lower()
            print("-" * 20)
            if search_choice in ["1", "name"]:
                search_by_name()
            elif search_choice in ["2", "id"]:
                search_by_id()
            elif search_choice in ["3", "email"]:
                search_by_email()
            elif search_choice in ["4", "status"]:
                search_by_status()
            else:
                print("Invalid choice.")
                time.sleep(2)
                clear_screen()
        else:
            print("No members available.")
            time.sleep(2)
            clear_screen()

    elif choice == "4":
        save_members_to_file()
        print("Exiting...")
        time.sleep(2)
        break

    else:
        print("Invalid choice. Please try again.")
        time.sleep(2)
        clear_screen()
