import random

doors = [1, 2, 3]
car = random.randint(1, 3)

while True:
    selected = int(input("Enter the door number you are selecting (1, 2, or 3): "))
    if selected not in doors:
        print("Invalid door number. Please enter 1, 2, or 3.")
    else:
        break

# Open one door that doesn't have the car
available_doors = [door for door in doors if door != selected and door != car]
opened_door = random.choice(available_doors)

print("The host opened Door", opened_door, "which has a goat.")

while True:
    switch = input("Do you want to switch doors? (yes/no): ")
    if switch.lower() not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
    else:
        break

# Determine the final selected door
if switch.lower() == "yes":
    selected = (set(doors) - set([selected, opened_door])).pop()

# Check if the final selected door has the car
if selected == car:
    print("Congratulations! You won the car!")
else:
    print("Sorry, you didn't win the car. The car was behind Door", car)
