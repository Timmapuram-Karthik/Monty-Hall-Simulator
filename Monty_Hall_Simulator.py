import random
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

top = Tk()
top.title("Monty Hall Simulator")
top.geometry("500x500")

#Initialize the doors for each game
def initialize_doors():
    return [1, 2, 3]

#Simulate the host opening a door
def door_open(var):
    available_doors = [door for door in doors if door != var and door != car]
    opened_door = random.choice(available_doors)
    doors.remove(opened_door)
    messagebox.showinfo("Door Opened", f"The host opened Door {opened_door} which has a goat.")

#Handle the door switching logic and display the result
def switch_door(var):
    if var == car:
        messagebox.showinfo("Result", "Congratulations! You won the car!")
    else:
        messagebox.showinfo("Result", f"Sorry, you didn't win the car. The car was behind Door {car}")

#Play a game by initializing the doors and randomly assigning the car
def play_game():
    global doors, car
    doors = initialize_doors()
    car = random.choice(doors)

#Handle the selection of a door and the subsequent actions
def select_door():
    selected_door = var.get()
    if selected_door == 0:
        messagebox.showinfo("Error", "Please select a door.")
        return
    door_open(selected_door)
    response = messagebox.askquestion("Switch Door", "Do you want to switch the door?")
    if response == "yes":
        switch_door([door for door in doors if door != selected_door][0])
    else:
        switch_door(selected_door)
    play_game()

# Load and display the image
image_path = "Monty_Hall_Image.jpg"
image = Image.open(image_path)
image = image.resize((470, 300))
image = ImageTk.PhotoImage(image)

image_label = Label(top, image=image)
image_label.grid(row=0, column=0, columnspan=3, padx=10, pady=20)

var = IntVar()

R1 = Radiobutton(top, text="Door 1", variable=var, value=1)
R1.grid(row=1, column=0, padx=10, pady=10)

R2 = Radiobutton(top, text="Door 2", variable=var, value=2)
R2.grid(row=1, column=1, padx=10, pady=10)

R3 = Radiobutton(top, text="Door 3", variable=var, value=3)
R3.grid(row=1, column=2, padx=10, pady=10)

B = Button(top, text="Select Door", command=select_door)
B.grid(row=2, column=0, columnspan=3, padx=10, pady=20)

# Initialize the doors and car for the first game
doors = initialize_doors()
car = random.choice(doors)

top.mainloop()
