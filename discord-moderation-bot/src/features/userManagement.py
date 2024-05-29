```python
# userManagement.py

class UserManagement:
    def __init__(self):
        self.user_data = {}  # Placeholder for user data storage

    def add_user(self, user_id, username):
        self.user_data[user_id] = {"username": username, "infractions": []}

    def remove_user(self, user_id):
        if user_id in self.user_data:
            del self.user_data[user_id]

    def get_user_infractions(self, user_id):
        if user_id in self.user_data:
            return self.user_data[user_id]["infractions"]
        return []

    def add_infraction(self, user_id, infraction_type, reason):
        if user_id in self.user_data:
            self.user_data[user_id]["infractions"].append({"type": infraction_type, "reason": reason})

    def clear_infractions(self, user_id):
        if user_id in self.user_data:
            self.user_data[user_id]["infractions"] = []

    def get_user_data(self, user_id):
        if user_id in self.user_data:
            return self.user_data[user_id]
        return None
```
This file implements the UserManagement class to handle user-related functionalities such as adding users, removing users, managing user infractions, and retrieving user data. The class stores user data in a dictionary with user IDs as keys and user details as values.