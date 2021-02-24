# IMPORTS
import tkinter as tk
import random




#CONSTANTS

#VARIABLE

# FUNCTIONS




#Main
root = tk.Tk()
root.geometry("1000x600")
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill='both')


#create image

#create a Button
button = tk.Button(root, text="START", width=20, height=3)
button.pack(padx=100, pady=110)


# call the draw cicle after 5 seconds
root.mainloop()