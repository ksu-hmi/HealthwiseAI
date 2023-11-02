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

        print("Login successful.")
        return True

    def modify_user_preference(self):
        # Prompt the user for their username, preference name, and preference value
        username = input("Enter your username: ")
        if username not in self.users:
            print("User not found.")
            return False

        preference_name = input("Enter the preference name: ")
        preference_value = input("Enter the preference value: ")

        user = self.users[username]
        # Modify the user's preference with the provided name and value
        user.add_preference(preference_name, preference_value)
        print("User preference modified successfully.")
        return True

    def get_user_preference(self):
        # Prompt the user for their username and the name of the preference to retrieve
        username = input("Enter your username: ")
        if username not in self.users:
            print("User not found.")
            return None

        preference_name = input("Enter the preference name: ")

        user = self.users[username]
        # Retrieve the user's specified preference
        return user.get_preference(preference_name)
    
    def modify_user_health_goal(self):
        # Get the username from the user
        username = input("Enter your username: ")
        if username not in self.users:
            print("User not found.")
            return False

        # Get the health goal name and value from the user
        goal_name = input("Enter the health goal name: ")
        goal_value = input("Enter the health goal value: ")

        # Find the user and add the health goal
        user = self.users[username]
        user.add_health_goal(goal_name, goal_value)
        print("User health goal modified successfully.")
        return True

    def get_user_health_goal(self):
        # Get the username from the user
        username = input("Enter your username: ")
        if username not in self.users:
            print("User not found.")
            return None

        # Get the health goal name from the user
        goal_name = input("Enter the health goal name: ")

        # Find the user and get the specified health goal
        user = self.users[username]
        return user.get_health_goal(goal_name)

    def modify_user_communication_preference(self):
        # Get the username from the user
        username = input("Enter your username: ")
        if username not in self.users:
            print("User not found.")
            return False

        # Get the communication preference name and value from the user
        preference_name = input("Enter the communication preference name: ")
        preference_value = input("Enter the communication preference value: ")

        # Find the user and add the communication preference
        user = self.users[username]
        user.add_communication_preference(preference_name, preference_value)
        print("User communication preference modified successfully.")
        return True

    def get_user_communication_preference(self):
        # Get the username from the user
        username = input("Enter your username: ")
        if username not in self.users:
            print("User not found.")
            return None

        # Get the communication preference name from the user
        preference_name = input("Enter the communication preference name: ")

        user = self.users[username]
        return user.get_communication_preference(preference_name)

    def schedule_appointment(self):
        # Get the username from the user
        username = input("Enter your username: ")
        if username not in self.users:
            print("User not found.")
            return False

        # Get appointment details from the user
        appointment_datetime = input("Enter the appointment datetime (YYYY-MM-DD HH:MM): ")
        doctor = input("Enter the doctor's name: ")
        location = input("Enter the location: ")

        appointment = {
            "datetime": datetime.strptime(appointment_datetime, "%Y-%m-%d %H:%M"),
            "doctor": doctor,
            "location": location
        }

        user = self.users[username]
        user.schedule_appointment(appointment)
        print("Appointment scheduled successfully.")
        return True

    def get_user_appointments(self):
        # Get the username from the user
        username = input("Enter your username: ")
        if username not in self.users:
            print("User not found.")
            return None

        user = self.users[username]
        return user.get_appointments()

    def add_user_activity(self):
        # Get the username from the user
        username = input("Enter your username: ")
        if username not in self.users:
            print("User not found.")
            return False

        # Get activity details from the user
        activity_datetime = input("Enter the activity datetime (YYYY-MM-DD HH:MM): ")
        activity_type = input("Enter the activity type: ")
        activity_duration = input("Enter the activity duration (in minutes): ")

        activity = {
            "datetime": datetime.strptime(activity_datetime, "%Y-%m-%d %H:%M"),
            "type": activity_type,
            "duration": int(activity_duration)
        }

        user = self.users[username]
        user.add_activity(activity)
        print("Activity added successfully.")
        return True

    def get_user_activities(self):
        # Get the username from the user
        username = input("Enter your username: ")
        if username not in self.users:
            print("User not found.")
            return None

        user = self.users[username]
        return user.get_activities()

    def add_user_notification(self):
        # Get the username from the user
        username = input("Enter your username: ")
        if username not in self.users:
            print("User not found.")
            return False

        # Get notification details from the user
        notification_datetime = datetime.now()
        notification_message = input("Enter the notification message: ")

        notification = {
            "datetime": notification_datetime,
            "message": notification_message
        }

        user = self.users[username]
        user.add_notification(notification)
        print("Notification added successfully.")
        return True

    def get_user_notifications(self):
        # Get the username from the user
        username = input("Enter your username: ")
        if username not in self.users:
            print("User not found.")
            return None

        user = self.users[username]
        return user.get_notifications()
    
healthwise_ai = HealthWiseAI()

# Register a user
healthwise_ai.register_user()

# Login a user
healthwise_ai.login_user()

# Modify user preferences
healthwise_ai.modify_user_preference()

# Get user preferences
healthwise_ai.get_user_preference()

# Modify user health goals
healthwise_ai.modify_user_health_goal()

# Get user health goals
healthwise_ai.get_user_health_goal()

# Modify user communication preferences
healthwise_ai.modify_user_communication_preference()

# Get user communication preferences
healthwise_ai.get_user_communication_preference()

# Schedule an appointment
healthwise_ai.schedule_appointment()

# Get user appointments
healthwise_ai.get_user_appointments()

# Add user activity
healthwise_ai.add_user_activity()

# Get user activities
healthwise_ai.get_user_activities()

# Add user notification
healthwise_ai.add_user_notification()

# Get user notifications
healthwise_ai.get_user_notifications()
   


