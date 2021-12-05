from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from PIL import ImageTk, Image
import tkinter as tk

root = Tk()
root.geometry("580x480")
root.title("Image Resizer")
root['bg'] = "#9C2D71"
root.iconbitmap("icon.ico")
root.resizable(False, False)

global intx
global inty

intx = IntVar()

inty = IntVar()



heightLabel = Label(root, text="Height: ", background="#9C2D71")
widthLabel = Label(root, text="Width: ", background="#9C2D71")

heightget = Entry(root, textvariable=intx)
widthget = Entry(root, textvariable=inty)


#intx.set(150)
#inty.set(404)

#newheight = str(heightget)
#newwidth = str(widthget)

widthLabel.place(x=215, y=315)
heightLabel.place(x=215, y=335)

widthget.place(x=260, y=315)
heightget.place(x=260, y=335)

def browseFunc():

    global image
    image = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("icon files", "*.ico")])
    
    imagetwo = Image.open(image)

    global next

    #resX = widthget.get()
    #resY = heightget.get()

    def it():

        if widthget.get() != ' ':
            global resX
            resX = int(widthget.get())
        if heightget.get() != ' ':
            global resY
            resY = int(heightget.get())

        global nextPic
        nextPic = imagetwo.resize((resX, resY), Image.ANTIALIAS)

    it()
    global resized

    resized = ImageTk.PhotoImage(nextPic)

    global imageLabel

    imageLabel = Label(root, image=resized, borderwidth=0, background="#9C2D71")
    if resX < 560 and resY < 300:
        imageLabel.pack(pady=10)
    else:
        previewFailLabel = Label(root, background="#9C2D71", text="Can't Preview the file because of been too large\n", font=("comis sans", 14))
        previewFailLabel.pack(pady=20)
    
#define function to save the resized file
def call():
    #del setOne
    #del setTwo
    print(image)

    intx.set(resX)
    inty.set(resY)
    #print(intx, inty)

    #print("found values for resX and resY are: ", resX, "/", resY)

    #imageLabel = browseFunc().imageLabel
    #imageLabel.pack()

    #here we need to save "nextPic" wich is the resized picture
    #save = filedialog.asksaveasfilename(filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
    nextPic.save(filedialog.asksaveasfilename(filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("icon files", "*.ico")]))


save = tk.Button(root, text="Save", command=call)
save.place(y=420, x=275)

browseButton = tk.Button(root, text="Browse Picture", command=browseFunc)
browseButton.place(x=255, y=360)

mainloop()