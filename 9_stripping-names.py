# Just to be clear, this program relates to stripping whitespace characters from a string

first_name = "\tMercedes\n     "
last_name = "     Williams     "

print(first_name + " " + last_name)
print("Left stripped: " + first_name.lstrip() + " " + last_name.lstrip())
print("Right stripped: " + first_name.rstrip() + " " + last_name.rstrip())
print("Fully stripped: " + first_name.strip() + " " + last_name.strip())