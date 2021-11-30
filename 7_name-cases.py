# Store a person's name in a variable, and then print that person's name 
# in lowercase, uppercase, and titlecase.

first_name = input("Enter first name: ")
first_name = first_name.lower().strip()

last_name = input("Enter last name: ")
last_name = last_name.lower().strip()

full_name = first_name + " " + last_name

print('\n' + "Lowercase: " + full_name.lower() + '\n' + "Uppercase: " + full_name.upper() + '\n' + "Titlecase: " + full_name.title())