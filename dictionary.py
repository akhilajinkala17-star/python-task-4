
user_profiles = {}


# Function to add a new user profile
def add_user(user_id, name):
    user_profiles[user_id] = name
    print(f"User {name} added successfully.")


# Function to retrieve a user's name by ID
def get_user(user_id):
    if user_id in user_profiles:
        return user_profiles[user_id]
    else:
        return "User ID not found."


# Function to update an existing user's name
def update_user(user_id, new_name):
    if user_id in user_profiles:
        user_profiles[user_id] = new_name
        print("User name updated successfully.")
    else:
        print("User ID not found. Update failed.")


# Function to remove a user profile
def remove_user(user_id):
    if user_id in user_profiles:
        del user_profiles[user_id]
        print("User removed successfully.")
    else:
        print("User ID not found. Removal failed.")


# Testing the functions

print("Initial Dictionary:")
print(user_profiles)


# Adding users
add_user(101, "Alice")
add_user(102, "Bob")
add_user(103, "Charlie")

print("\nDictionary after adding users:")
print(user_profiles)


# Retrieving users
print("\nRetrieving user with ID 102:")
print(get_user(102))

print("Retrieving user with ID 200:")
print(get_user(200))


# Updating user
print("\nUpdating user with ID 103:")
update_user(103, "David")

print("Dictionary after updating:")
print(user_profiles)


# Removing user
print("\nRemoving user with ID 101:")
remove_user(101)

print("Dictionary after removing:")
print(user_profiles)


# Trying to remove a non-existing user
print("\nRemoving user with ID 500:")
remove_user(500)

print("\nFinal Dictionary:")
print(user_profiles)