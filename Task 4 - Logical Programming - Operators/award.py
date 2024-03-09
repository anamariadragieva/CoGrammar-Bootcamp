"""
Design a program that determines the award a person competing in a triathlon will receive. 

Your program should read in minutes for all three events of a triathlon: swimming, cycling, running

Use an input() command to get the following information from the user.
convert all numerical input into integers
Name
Surname
Age
Gender
swimming_time
cycling_time
running_time
"""

name = input("What is your name? ")
surname = input("What is your last name? ")
age = int(input("How old are you? "))
gender = input("What is your gender? ")
swimming_time = int(input("How long did you swim for (in munutes)? "))
cycling_time = int(input("How long did you cycle for (in munutes)? "))
running_time = int(input("How long did you run for (in munutes)? "))

# calculate and display the total time taken to complete the triathlon.
total_time = swimming_time + cycling_time + running_time
print(f"The total time {name} {surname}, {gender}, aged {age} has taken to complete the triathlon is {total_time} minutes.")

"""
The award a participant receives is based on the total time taken to complete the triathlon.
The qualifying time for awards is 100 minutes.
Display the award that the participant will receive based on the following criteria:
"""

# if the  total time is under 100 minutes, the award is Provincial Colours
if total_time <= 100:
    print(f"Congratulations, {name}! You completed the triathlon within the qualifying time. You're awarded Provincial Colours!")
  
# if the  total time is between 101 - 105 minutes, the award is Provincial Half Colours
elif total_time <= 105:
    print(f"Congratulations, {name}! You completed the triathlon within 5 minutes of the qualifying time. You're awarded Provincial Half Colours!")
  
# if the  total time is between 106 - 110 minutes, the award is Provincial Scroll
elif total_time <= 110:
    print(f"Congratulations, {name}! You completed the triathlon within 10 minutes of the qualifying time. You're awarded Provincial Scroll!")

# if the  total time is 111 minutes or more, there is no award
else:
    print(f"Sorry, {name}! You did not complete the triathlon within the qualifying time. Keep practising for the next one!")
  
