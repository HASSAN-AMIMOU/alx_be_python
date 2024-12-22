# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on its priority and time sensitivity using match-case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". Consider tackling it soon."
    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " that requires attention soon."
        else:
            reminder += ". Schedule it for later."
    case "low":
        reminder = f"'{task}' is a low priority task"
        if time_bound == "yes":
            reminder += " but it's not time-sensitive."
        else:
            reminder += ". Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority input. Please use 'high', 'medium', or 'low'."

# Print the reminder
print(f"Reminder: {reminder}")
