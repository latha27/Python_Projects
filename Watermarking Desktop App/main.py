from tkinter import *
from PIL import Image
# loading Python Imaging Library
from PIL import ImageTk, Image, ImageFont, ImageDraw

# To get the dialog box to open when required
from tkinter import filedialog

BACKGROUND_COLOR = "#B1DDC6"

global img
global img2

def close_app():
    window.quit()

def select_images():
    global img
    global myvar
    # Select the Imagename  from a folder
    x = openfilename()
    # opens the image
    img = Image.open(x)
    # resize the image and apply a high-quality down sampling filter
    img = img.resize((250, 250), Image.ANTIALIAS)
    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)

    #upload_image = canvas.create_image(0, 0, image=img, anchor=NW)
    #canvas.grid(row=1, column=1)



    def addtext():
        my_image = Image.open(x)
        text_font = ImageFont.truetype("arial.ttf", 46)
        text_to_add = my_entry.get()

        edit_image = ImageDraw.Draw(my_image)
        edit_image.text((200, 150), text_to_add, ("green"), font=text_font)

        my_image.save("edited_photo.png")
        my_entry.delete(0, END)
        my_entry.insert(0, "Saving File...")

        my_label.after(1000, show_pic)

    def show_pic():
        global img2
        img1 = Image.open("edited_photo.png")
        img1 = img1.resize((250, 250), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(img1)
        my_label.config(image=img2)

        my_entry.delete(0, END)


    def removewatermark():
        canvas.delete(img2)
        my_label.config(image=img)

    def clear():
        my_label.destroy()
        my_entry.destroy()

    clear_images = Button(window, text="Clear", command=clear)
    clear_images.grid(row=3, column=0, sticky=W, pady=2)

    my_label = Label(canvas, image=img)
    my_label.grid(pady=20)

    my_entry = Entry(canvas, font=("Helvetica", 24))
    my_entry.grid(pady=20)

    add_text = Button(canvas, text="Add Text To Image", command=addtext, font=("Helvetica", 24))
    add_text.grid(row=4, column=0, sticky=W, pady=2)

    remove_watermark = Button(canvas, text="Remove Watermark", command=removewatermark)
    remove_watermark.grid(row=6, column=0, sticky=W, pady=2)


def openfilename():
    # open file dialog box to select image
    # The dialogue box has a title "Open"
    filename = filedialog.askopenfilename(title='"pen')
    return filename


window = Tk()
window.title("Image WaterMark")


window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

close_button = Button(window, text="Close App", command=close_app)
close_button.grid(row=1, column=0, sticky=W, pady=2)

select_images = Button(window, text="Select Image", command=select_images)
select_images.grid(row=2, column=0, sticky=W, pady=2)




#Entry Box

canvas = Canvas(width=600, height=600)

'''# Create A Label
my_label = Label(canvas, image=img)
my_label.grid(pady=20)

#Entry Box
my_entry = Entry(canvas, font=("Helvetica", 24))
my_entry.grid(pady=20)'''

canvas.grid(row=0, column=1, columnspan=8, rowspan=8, padx=5, pady=5)






window.mainloop()
