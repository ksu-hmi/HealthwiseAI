import argon2
import secrets

class HealthWiseAI:
    def __init__(self):
        self.users = {}  # Store user data in a dictionary

    def register_user(self, username, password):
        if username in self.users:
            print("Username already exists. Please choose a different username.")
            return False
 
        # Generate a random salt
        salt = secrets.token_hex(32)

        # Hash the password with the salt using a strong hashing algorithm like Argon2
        password_hasher = argon2.PasswordHasher()
        hashed_password = password_hasher.hash(password)

        # Store the user data in the dictionary
        self.users[username] = {'hashed_password': hashed_password, 'salt': salt}

        print("Registration successful.")
        return True

    def login_user(self, username, password):
        if username not in self.users:
            print("Invalid username or password. Please try again.")
            return False

        # Retrieve the user data from the dictionary
        stored_password = self.users[username]['hashed_password']
        salt = self.users[username]['salt']

        # Verify the provided password against the stored hashed password
        password_hasher = argon2.PasswordHasher()
        try:
            password_hasher.verify(stored_password, password)
        except argon2.exceptions.VerifyMismatchError:
            print("Invalid username or password. Please try again.")
            return False

        # Return the user object
        return self.users[username]

# Example usage
healthwise_ai = HealthWiseAI()

# Accept user input for registration
username = input("Enter your username: ")
password = input("Enter your password: ")
healthwise_ai.register_user(username, password)

# Try logging in with the correct credentials
user_data = healthwise_ai.login_user(username, password)

# Access the user data if the login is successful
if user_data:
    print(f"User data for '{username}': {user_data}") 
