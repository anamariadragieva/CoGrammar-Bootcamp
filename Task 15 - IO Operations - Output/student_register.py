# Ask the user how many students are registering
num_students = int(input("How many students are registering? "))

# Open the file in write mode
with open("reg_form.txt", "w", encoding="utf-8") as file:
    
    for i in range(1, num_students + 1):
        student_id = input(f"Enter student {i}'s ID number: ")
        file.write(student_id + ": " + "_" * 20 + "\n\n")
        #file.write("-" * 20 + "\n\n")

with open("reg_form.txt", "r", encoding="utf-8") as file:
    print(f"\nRegistered students:\n\n{file.read()}")
 
   
