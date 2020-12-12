from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
from pyautogui import prompt
import pickle
from tkinter.colorchooser import askcolor
prev_x = 0
prev_y = 0
x = 0
y = 0
created_element_info = []
new = []
created = []
shape = "Line"
color = "blue"
eraser_on = False
line_width = 3


def saveDrawingFile(e=""):
    global created_element_info
    filename = asksaveasfilename(initialfile="drawing" ,defaultextension=".pkl", filetypes=[("Pickle Files", "*.pkl")])
    if filename != None: 
        with open(filename, "wb") as f:
            pickle.dump(created_element_info, f)


def colorPicker(e=""):
    global color, eraser_on
    eraser_on = False
    color = askcolor(color=color)[1]
    root.config(cursor=f'cursor {color} {color}', insertbackground=f"{color}")


def shapechanger(e=""):
    global shape
    shape = radiovalue.get()


def createElms():
    global shape
    if shape == "Rectangle":
        a = canvas.create_rectangle(prev_x, prev_y, x, y, fill=color)
    elif shape == "Oval":
        a = canvas.create_oval(prev_x, prev_y, x, y, fill=color)
    elif shape == "Polygan":
        a = canvas.create_polygon(
            prev_x, prev_y, x, y, prev_x, prev_y, fill=color)
    elif shape == "Arc":
        a = canvas.create_arc(prev_x, prev_y, x, y, fill=color)
    elif shape == "Text":
        text = prompt("Enter the text")
        a = canvas.create_text(x, y, fill=color, font=f"Times {abs(y-prev_y)} italic bold",
                            text=text)
    else:
        a = canvas.create_line(prev_x, prev_y, x, y,
                               width=line_width, fill=color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=3)
    return a

def createLine(e=""):
    global x, y, created, new, color, line_width
    try:
        if e != "Get":
            x = e.x
            y = e.y
        status.set(f"Position : x - {x} , y - {y}")
        statusbar.update()
        a = createElms()
        if e != "Get":
            created.append(a)
            for item in created[:-1]:
                canvas.delete(item)
    except Exception as e:
        tmsg.showerror("Some Error Occurred!", e)


def captureMotion(e=""):
    status.set(f"Position : x - {e.x} , y - {e.y}")
    statusbar.update()


def recordPosition(e=""):
    global prev_x
    global prev_y
    print("Updated!")
    prev_x = e.x
    prev_y = e.y


def saveDrawing(e=""):
    global created, shape, color
    global created_element_info
    new.append(created[-1])
    created = []
    created_element_info_new = {
        "type": shape,
        "color": color,
        "prev_x": prev_x,
        "prev_y": prev_y,
        "x": x,
        "y": y
    }
    created_element_info.append(created_element_info_new)
    # print(created_element_info)


def setlinewidth(e=""):
    global line_width
    line_width = scale.get()


def clearCanvas(e=""):
    global created_element_info, canvas, created, new
    canvas.delete("all")
    created_element_info = []
    created = []
    new = []


def getsavedrawing():
    global x, y, prev_x, prev_y, shape, color
    filename = askopenfilename(defaultextension=".pkl", filetypes = [("Pickle Files", "*.pkl")])
    if filename != None:
        with open(filename, "rb") as f:
            data = pickle.load(f)
            for draw_info in data:
                x = draw_info["x"]
                y = draw_info["y"]
                prev_x = draw_info["prev_x"]
                prev_y = draw_info["prev_y"]
                shape = draw_info["type"]
                color = draw_info["color"]
                createElms()


root = Tk()
root.title("Drawing Pad - Created By Fahad")
# root.geometry("600x300")
root.minsize(600, 300)
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400
canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
# canvas.create_line(0,0,300,100, fill="red")
canvas.pack()
canvas.bind("<1>", recordPosition)
canvas.bind("<B1-Motion>", createLine)
canvas.bind("<ButtonRelease-1>", saveDrawing)
canvas.bind("<Motion>", captureMotion)
radiovalue = StringVar()
radiovalue.set("Line")
geometry_shapes = ["Line", "Rectangle", "Arc", "Oval", "Text"]
frame = Frame(root)
frame.pack(side=BOTTOM)
for shape in geometry_shapes:
    radio = Radiobutton(frame, text=shape, variable=radiovalue, font="comicsans 12 bold",
                        value=shape, command=shapechanger).pack(side=LEFT, padx=6, pady=3)
Button(frame, text="Save", font="comicsans 12 bold",
       command=saveDrawingFile).pack(side=BOTTOM, padx=6, pady=6)
Button(frame, text="Clear", font="comicsans 12 bold",
       command=clearCanvas).pack(side=BOTTOM, padx=6)
Button(frame, text="Color", font="comicsans 12 bold",
       command=colorPicker).pack(side=BOTTOM, padx=6)
Button(frame, text="Get", font="comicsans 12 bold",
       command=getsavedrawing).pack(side=BOTTOM, padx=6)
scale = Scale(root, from_=1, to=20, orient=HORIZONTAL, command=setlinewidth)
scale.pack(side=BOTTOM)
# Status bar=
status = StringVar()
status.set("Position : x - 0 , y - 0")
statusbar = Label(root, textvariable=status, anchor="w", relief=SUNKEN)
statusbar.pack(side=BOTTOM, fill=X)
root.mainloop()
