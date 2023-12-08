from tkinter import *
from PIL import ImageTk, Image

def text_to_binary():
    result_text.delete("1.0", END)
    plain_text = enter1.get("1.0", END).strip()
    binary_text = ' '.join(format(ord(char), 'b') for char in plain_text)
    result_text.insert(END, binary_text)

def binary_to_text():
    result_text.delete("1.0", END)
    binary_text = enter1.get("1.0", END).strip().split()
    text = ''.join(chr(int(char, 2)) for char in binary_text)
    result_text.insert(END, text)

win = Tk()
win.title("Binary Converter with GUI")

# Load the image file
background_image = Image.open("C:/Users/hp/Desktop/Binary-Encode-Decode/images.jpeg")

# Resize the image to fit the window size
width, height = win.winfo_screenwidth(), win.winfo_screenheight()
resized_image = background_image.resize((width, height))

# Convert the resized image to a Tkinter-friendly format
background_photo = ImageTk.PhotoImage(resized_image)

# Create a label and set it as the background image
background_label = Label(win, image=background_photo)
background_label.place(x=0, y=0)

# Edit the window's geometry
new_width = 600
new_height = 650
x_position = (win.winfo_screenwidth() // 2) - (new_width // 2)
y_position = (win.winfo_screenheight() // 2) - (new_height // 2)

win.geometry(f"{new_width}x{new_height}+{x_position}+{y_position}")

label1 = Label(win, text="Enter your Text", font=("Times New Roman", 25, "bold"), bg="black", fg="red")
label1.place(x=20, y=20, height=40, width=400)

enter1 = Text(win, font=("Times New Roman", 15), bg="black", fg="lime")
enter1.place(x=20, y=90, height=300, width=550)

btn_encode = Button(win, text="Text to Binary", font=("Times New Roman", 20), bg="blue", fg="lime", command=text_to_binary)
btn_encode.place(x=40, y=420, height=50, width=220)

btn_decode = Button(win, text="Binary to Text", font=("Times New Roman", 20), bg="black", fg="lime", command=binary_to_text)
btn_decode.place(x=340, y=420, height=50, width=220)

result_text = Text(win, font=("Times New Roman", 15), bg="black", fg="lime")
result_text.place(x=20, y=500, height=130, width=550)

win.mainloop()
