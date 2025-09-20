from pymongo import MongoClient

# 1️⃣ Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["myDatabase"]  # Use your existing DB
collection = db["users"]

print("Connected to MongoDB successfully!\n")


# 2️⃣ CREATE - Insert a new user
def create_user():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    email = input("Enter email: ")

    user = {"name": name, "age": age, "email": email}
    collection.insert_one(user)
    print(f"User '{name}' inserted successfully!\n")


# 3️⃣ READ - View users
def read_users():
    print("\nAll users in database:")
    for user in collection.find():
        print(user)
    print()


# 4️⃣ UPDATE - Modify a user
def update_user():
    name = input("Enter the name of user to update: ")
    field = input("Enter field to update (name/age/email): ")
    value = input("Enter new value: ")

    # Convert age to int if updating age
    if field == "age":
        value = int(value)

    result = collection.update_one({"name": name}, {"$set": {field: value}})
    if result.matched_count:
        print(f"User '{name}' updated successfully!\n")
    else:
        print(f"No user found with name '{name}'\n")


# 5️⃣ DELETE - Remove a user
def delete_user():
    name = input("Enter the name of user to delete: ")
    result = collection.delete_one({"name": name})
    if result.deleted_count:
        print(f"User '{name}' deleted successfully!\n")
    else:
        print(f"No user found with name '{name}'\n")


# 6️⃣ Interactive menu
def menu():
    while True:
        print("===== MongoDB CRUD Menu =====")
        print("1. Insert User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            create_user()
        elif choice == "2":
            read_users()
        elif choice == "3":
            update_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.\n")


# Run the menu
if __name__ == "__main__":
    menu()
