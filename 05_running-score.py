score = 0
update = 0

print("Enter a positive integer to add to score")
print("Enter a negative integer when finished")

while (update >= 0):
    print("Current score: ", score)
    update = int(input("Plus: "))
    if update > 0:
        score += update

print("Final score: ", score)
