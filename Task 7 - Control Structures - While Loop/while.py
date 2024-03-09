sum = 0
count = 0
user_input = 0

# Continuously ask the user to enter a number
while user_input != -1:
    user_input = int(input("Enter a number (enter -1 to stop): "))

    # Check if the user wants to stop
    if user_input == -1:
        break

    # If not, update sum and count
    number = int(user_input)
    sum += number
    count += 1

# Check if any numbers were entered before calculating the average
if count > 0:
    average = sum / count
    print(f"Average of all numbers entered (excluding -1) is {average}")
else:
    print("No numbers were entered.")