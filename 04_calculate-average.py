sum = 0

iteration_count = int(input("Calculate average of how many numbers: "))

for _ in range(iteration_count):
    num = int(input("Enter an integer: "))
    sum += num

print("The average of these numbers is: ", sum / iteration_count)