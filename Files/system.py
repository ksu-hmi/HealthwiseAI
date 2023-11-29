import hashlib
import secrets
from datetime import datetime

class User:
    def __init__(self, username, password):
        self.username = username
        self.salt = secrets.token_hex(16)  # Generate a random salt for password hashing
        self.hashed_password = self._hash_password(password)  # Hash the provided password
        self.preferences = {}  # Initialize an empty dictionary for user preferences
        self.health_goals = {}  # Initialize an empty dictionary for health goals
        self.communication_preferences = {}  # Initialize an empty dictionary for communication preferences
        self.appointments = []  # Initialize an empty list for user appointments
        self.activities = []  # Initialize an empty list for user activities
        self.notifications = []  # Initialize an empty list for user notifications

    def _hash_password(self, password):
        # Hash the password using PBKDF2 with the generated salt and 100,000 iterations
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), bytes.fromhex(self.salt), 100000)
        return hashed_password.hex()

    # Methods for managing user preferences
    def add_preference(self, preference_name, preference_value):
        self.preferences[preference_name] = preference_value

    def get_preference(self, preference_name):
        return self.preferences.get(preference_name)

    # Methods for managing user health goals
    def add_health_goal(self, goal_name, goal_value):
        self.health_goals[goal_name] = goal_value

    def get_health_goal(self, goal_name):
        return self.health_goals.get(goal_name)

    # Methods for managing communication preferences
    def add_communication_preference(self, preference_name, preference_value):
        self.communication_preferences[preference_name] = preference_value

    def get_communication_preference(self, preference_name):
        return self.communication_preferences.get(preference_name)

    # Methods for managing user appointments
    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)

    def get_appointments(self):
        return self.appointments

    # Methods for managing user activities
    def add_activity(self, activity):
        self.activities.append(activity)

    def get_activities(self):
        return self.activities

    # Methods for managing user notifications
    def add_notification(self, notification):
        self.notifications.append(notification)

    def get_notifications(self):
        return self.notifications

    # Method for user login authentication
    def login(self, password):
        hashed_password = self._hash_password(password)
        return hashed_password == self.hashed_password


class HealthWiseAI:
    def __init__(self):
        self.users = {}  # Initialize an empty dictionary to store user objects
        self.current_username = None  # Track the current username for interactions

    # Helper method to get the current user
    def get_current_user(self):
        if self.current_username is None or self.current_username not in self.users:
            print("User not found.")
            return None
        return self.users[self.current_username]

    # Method to register a new user
    def register_user(self):
        username = input("Enter a username: ")  # Prompt the user to input a username
        password = input("Enter a password: ")  # Prompt the user to input a password

        if username in self.users:
            print("Username already exists. Please choose a different username.")
            return False

        user = User(username, password)  # Create a new User object with the provided username and password
        self.users[username] = user  # Add the user to the dictionary of users
        print("Registration successful.")
        return True

    def login_user(self):
        # Prompt the user for their username and password
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username not in self.users:
            print("Invalid username or password. Please try again.")
            return False

        user = self.users[username]
        # Validate the user's login credentials
        if not user.login(password):
            print("Invalid username or password. Please try again.")
            return False

        # Set the current username for subsequent interactions
        self.current_username = username
        print("Login successful.")
        return True

    def modify_user_preference(self):
        # Prompt the user for the preference name and value
        preference_name = input("Enter the preference name: ")
        preference_value = input("Enter the preference value: ")

        user = self.get_current_user()
        if user is not None:
            # Modify the user's preference with the provided name and value
            user.add_preference(preference_name, preference_value)
            print("User preference modified successfully.")
        return True

    def get_user_preference(self):
        # Prompt the user for the preference name to retrieve
        preference_name = input("Enter the preference name: ")

        user = self.get_current_user()
        if user is not None:
            # Retrieve the user's specified preference
            return user.get_preference(preference_name)
        return None
    
    def modify_user_health_goal(self):
        # Prompt the user for the health goal name and value
        goal_name = input("Enter the health goal name: ")
        goal_value = input("Enter the health goal value: ")

        user = self.get_current_user()
        if user is not None:
            # Add or modify the user's health goal with the provided name and value
            user.add_health_goal(goal_name, goal_value)
            print("User health goal modified successfully.")
        return True

    def get_user_health_goal(self):
        # Prompt the user for the health goal name to retrieve
        goal_name = input("Enter the health goal name: ")

        user = self.get_current_user()
        if user is not None:
            # Retrieve the user's specified health goal
            return user.get_health_goal(goal_name)
        return None

    def modify_user_communication_preference(self):
        # Prompt the user for the communication preference name and value
        preference_name = input("Enter the communication preference name: ")
        preference_value = input("Enter the communication preference value: ")

        user = self.get_current_user()
        if user is not None:
            # Modify the user's communication preference with the provided name and value
            user.add_communication_preference(preference_name, preference_value)
            print("User communication preference modified successfully.")
        return True

    def get_user_communication_preference(self):
        # Prompt the user for the communication preference name to retrieve
        preference_name = input("Enter the communication preference name: ")

        user = self.get_current_user()
        if user is not None:
            # Retrieve the user's specified communication preference
            return user.get_communication_preference(preference_name)
        return None

    def schedule_appointment(self):
        # Prompt the user for appointment details
        appointment_datetime = input("Enter the appointment datetime (YYYY-MM-DD HH:MM): ")
        doctor = input("Enter the doctor's name: ")
        location = input("Enter the location: ")

        user = self.get_current_user()
        if user is not None:
            # Schedule an appointment for the current user
            appointment = {
                "datetime": datetime.strptime(appointment_datetime, "%Y-%m-%d %H:%M"),
                "doctor": doctor,
                "location": location
            }
            user.schedule_appointment(appointment)
            print("Appointment scheduled successfully.")
        return True

    def get_user_appointments(self):
        user = self.get_current_user()
        if user is not None:
            # Retrieve the user's appointments
            return user.get_appointments()
        return None

# Instantiate the HealthWiseAI class
healthwise_ai = HealthWiseAI()

# Example usage:
healthwise_ai.register_user()
healthwise_ai.login_user()
healthwise_ai.modify_user_preference()
preference = healthwise_ai.get_user_preference()
print("User preference:", preference)
healthwise_ai.modify_user_health_goal()
goal = healthwise_ai.get_user_health_goal()
print("User health goal:", goal)
healthwise_ai.modify_user_communication_preference()
communication_preference = healthwise_ai.get_user_communication_preference()
print("User communication preference:", communication_preference)
healthwise_ai.schedule_appointment()
appointments = healthwise_ai.get_user_appointments()
print("User appointments:", appointments)
