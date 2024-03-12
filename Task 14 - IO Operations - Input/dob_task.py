# Read data from DOB.txt
with open('DOB.txt', 'r') as file:
    lines = file.readlines()

# Separate names and birthdates
names = []
birthdates = []

for line in lines:
    data = line.strip().split(' ')
    name = ' '.join(data[:-3])  # Joining first name + last name
    birthdate = ' '.join(data[-3:]) # Joining day + month + year

    names.append(name)
    birthdates.append(birthdate)

# Print names
print("\nName")
for name in names:
    print(name)

# Print birthdates
print("\nBirthdate")
for birthdate in birthdates:
    print(birthdate)