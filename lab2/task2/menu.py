from container import Container

print("Enter 0 to exit")
print("Enter 1 to add")
print("Enter 2 to remove")
print("Enter 3 to find")
print("Enter 4 to list")
print("Enter 5 to grep")
print("Enter 6 to save")
print("Enter 7 to load")
print("Enter 8 to switch")

students = {
    "Vadim": {"1", "2", "3", "4", "5"},
    "Denis": {"6", "7", "8", "9"},
    "Egor": {"10", "11", "12", "13"}
}

containerized_students = Container(students)


def menu(users):
    username = str(input("Enter username: "))
    users.switch(username)

    while True:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            added_data = str(input("Enter data to add: "))
            users.add(added_data)
        elif choice == 2:
            removed_data = str(input("Enter data to remove: "))
            users.remove(removed_data)
        elif choice == 3:
            found_data = str(input("Enter data to find: "))
            print(users.find(found_data))
        elif choice == 4:
            print(users.list())
        elif choice == 5:
            regex = str(input("Enter a regular expression to find: "))
            print(users.grep(regex))
        elif choice == 6:
            users.save()
        elif choice == 7:
            temp_dict = users.load()
            print(temp_dict)
        elif choice == 8:
            switched_username = str(input("Enter username to switch: "))
            users.switch(switched_username)
        elif choice == 0:
            break
        else:
            print("Incorrect input")


menu(containerized_students)
