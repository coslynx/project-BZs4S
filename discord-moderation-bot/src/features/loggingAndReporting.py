loggingAndReporting.py:

```python
# File: loggingAndReporting.py

import json

class LoggingAndReporting:
    def __init__(self):
        self.moderation_logs = {}
        self.user_infractions = {}

    def load_moderation_logs(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.moderation_logs = json.load(file)
        except FileNotFoundError:
            print("Moderation logs file not found. Creating new file.")
            self.save_moderation_logs(file_path)

    def save_moderation_logs(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.moderation_logs, file, indent=4)

    def log_moderation_action(self, user_id, action, reason):
        self.moderation_logs[user_id] = {"action": action, "reason": reason}
    
    def load_user_infractions(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.user_infractions = json.load(file)
        except FileNotFoundError:
            print("User infractions file not found. Creating new file.")
            self.save_user_infractions(file_path)

    def save_user_infractions(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.user_infractions, file, indent=4)

    def add_infraction(self, user_id, infraction_type):
        if user_id in self.user_infractions:
            self.user_infractions[user_id].append(infraction_type)
        else:
            self.user_infractions[user_id] = [infraction_type]
```

Dependencies:
- This file depends on the existence of moderationLogs.json and userInfractions.json in the data directory for loading and saving data.