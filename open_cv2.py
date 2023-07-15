







import cv2
import numpy as np
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

def image_from_camera(path_image):
    global image, original_image

    image = cv2.imread(path_image)
    original_image = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(image)
    pil_image = pil_image.resize((250, 250), Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(pil_image)

    img_label.configure(image=img_tk)
    img_label.image = img_tk
    img_label2.pack_forget()  # Remove the image label widget


    for button in buttons:
        button.configure(state="normal")


def caemra():
    import cv2
    cap = cv2.VideoCapture(0)
    num = 0
    while cap.isOpened():
        succes, img = cap.read()
        k = cv2.waitKey(5)
        if k == 27:
            break
        elif k == ord('s'): 
            cv2.imwrite('image' + str(num) + '.jpg', img)
            print("image saved!")
            num += 1
            cv2.destroyAllWindows()
            image_from_camera('image0.jpg')
            break
        cv2.imshow('Caemra',img)

def button_click(button_number):
    global image, original_image

    if button_number == 0:
        # image = cv2.resize(image, None, fx=0.5, fy=0.5)
        image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    elif button_number == 1:
        image = cv2.flip(image, 1)
    elif button_number == 2:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    elif button_number == 3:
        image = cv2.GaussianBlur(image, (7, 7), 0)
    elif button_number == 4:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.Canny(gray_image, 100, 200)
    elif button_number == 5:
        
        image = cv2.medianBlur(image,5)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    update_img_label()

def update_img_label():
    global image, img_label

    pil_image = Image.fromarray(image)
    pil_image = pil_image.resize((250, 250), resample=Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(pil_image)

    img_label.configure(image=img_tk)
    img_label.image = img_tk

def upload_image():
    global image, original_image

    filename = filedialog.askopenfilename(initialdir="/", title="Select Image", filetypes=(("Image Files", "*.jpg;*.jpeg;*.png"), ("All Files", "*.*")))
    image = cv2.imread(filename)
    original_image = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(image)
    pil_image = pil_image.resize((250, 250), resample=Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(pil_image)

    img_label.configure(image=img_tk)
    img_label.image = img_tk
    img_label2.pack_forget()  # Remove the image label widget


    for button in buttons:
        button.configure(state="normal")

# def button_enter(event):
#     event.widget.configure(bg='#2AE1FA')

# def button_leave(event):
#     event.widget.configure(bg='SystemButtonFace')


def button_enter(event):
    event.widget.configure(bg='#2AE1FA')
    event.widget.configure(relief=SUNKEN)

def button_leave(event):
    event.widget.configure(bg='lightgray')
    event.widget.configure(relief=RAISED)


window = Tk()
window.geometry("750x400")
window.title("Image Processing")
window.iconbitmap(r"./images/logo.ico")
window.configure(bg='#69E376')


# Center the window on the screen
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Set the background image
# background_image = Image.open("f.png")
# background_image = background_image.resize((window_width, window_height), Image.ANTIALIAS)
# background_photo = ImageTk.PhotoImage(background_image)
# background_label = Label(window, image=background_photo,)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Prevent resizing of the window
window.resizable(False, False)


image_path = "bg.png"
image = Image.open(image_path)
image = image.resize((120, 100))
tk_image = ImageTk.PhotoImage(image)
img_label_logo = Label(window, image=tk_image)
img_label_logo.place(x=1, y=1)


# Create a frame to hold the top section (image, camera button, select button)
# top_frame = Frame(window,bg="#4BC9A9",width=200, height=200)
# top_frame.pack()
top_frame = Frame(window, bg="", bd=5, highlightthickness=0)

top_frame.place(relx=0.5, rely=0.45, anchor=CENTER)


img_label = Label(top_frame, foreground="white", background="#69E376")
img_label.pack(side="left", padx=10, pady=10)

img_label2 = Label(top_frame, height=15,width=30,foreground="white",bd=10, background="#28CA39")
img_label2.pack(side="left", padx=10, pady=10)


upload_button = Button(top_frame, text="Select Image", command=upload_image,font=("Arial", 12,'bold'))
upload_button.pack(side="left", padx=10, pady=10)

camera_button = Button(top_frame, text="Camera", command=caemra,font=("Arial", 12,'bold'))
camera_button.pack(side="left", padx=10, pady=10)

# Create a frame to hold the bottom section (buttons)
bottom_frame = Frame(window,bg="#4BC9A9")
bottom_frame.place(x=30,y=350)

filters = ["Rotate Horizontally", "Flip", "Grayscale", "Gaussian blur", "Edge Detection",'Smothing']
buttons = []
for i in range(0, 6):
    button = Button(bottom_frame, text=f"{filters[i]}".format(i), state="disabled", command=lambda i=i: button_click(i),font=("Arial", 12,'bold'))
    button.pack(side="left", padx=5, pady=5)
    button.bind('<Enter>', button_enter) 
    button.bind('<Leave>', button_leave)  
    buttons.append(button)


camera_button.bind('<Enter>', button_enter) 
camera_button.bind('<Leave>', button_leave)  

upload_button.bind('<Enter>', button_enter)  
upload_button.bind('<Leave>', button_leave)  


window.mainloop()

