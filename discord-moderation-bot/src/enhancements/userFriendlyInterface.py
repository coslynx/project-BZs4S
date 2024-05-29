```python
# userFriendlyInterface.py

def display_welcome_message():
    print("Welcome to the Discord Moderation Bot!")
    print("Use the following commands to interact with the bot:")

def display_help_command():
    print("List of available commands:")
    print("!mute @user - Mute a user")
    print("!kick @user - Kick a user")
    print("!ban @user - Ban a user")
    print("!warn @user - Warn a user")
    print("!set_rules - Set custom rules")
    print("!set_thresholds - Set custom thresholds")
    print("!adjust_sensitivity - Adjust filter sensitivity")
    print("!customize_responses - Customize automated responses")

def display_error_message():
    print("Error: Invalid command. Please try again.")

def display_success_message(action):
    print(f"{action.capitalize()} successfully executed.")

def display_user_infractions(user_infractions):
    print("User Infractions:")
    for user, infractions in user_infractions.items():
        print(f"{user}: {infractions}")

def display_moderation_logs(moderation_logs):
    print("Moderation Logs:")
    for log in moderation_logs:
        print(log)

def display_report(report):
    print("User Behavior Report:")
    for user, behavior in report.items():
        print(f"{user}: {behavior}")
```
Explanation:
- The userFriendlyInterface.py file contains functions to display welcome messages, help commands, error messages, success messages, user infractions, moderation logs, and user behavior reports.
- These functions are essential for providing a user-friendly interface for interacting with the Discord moderation bot.
- The functions ensure clear communication with the users and enhance the overall user experience when using the bot.
- The functions are designed to be self-contained and can be easily called from other parts of the bot for displaying information to the users.