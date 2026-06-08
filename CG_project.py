import numpy as np
import turtle
import tkinter as tk
import tkinter.messagebox as msgbox

vertices = []

#turtle screen
screen = turtle.Screen()
screen.title("ReflectX")
screen.setup(width=718, height=787)
screen.bgcolor("#2e2e2e")  # Dark theme

#axes and grid
turtle.tracer(0)
axes_drawer = turtle.Turtle()
axes_drawer.hideturtle()
axes_drawer.speed(0)
axes_drawer.pensize(1)

#drawing shapes
drawer = turtle.Turtle()
drawer.penup()
drawer.speed()
drawer.pensize(2)
drawer.hideturtle()

canvas = screen.getcanvas()
root = canvas.winfo_toplevel()

snap_to_grid = tk.BooleanVar(value=False)
reflection_mode = tk.StringVar(value="free")

try:
    root.iconbitmap("axes.ico")
except:
    pass

# Theme
bg_color = "#2e2e2e"
fg_color = "#ffffff"
btn_bg = "#444444"
btn_fg = "#ffffff"
highlight = "#666666"

label_style = {"bg": bg_color, "fg": fg_color, "font": ("Arial", 10)}
entry_style = {"bg": "#3a3a3a", "fg": "#ffffff", "insertbackground": "#ffffff"}
button_style = {"bg": btn_bg, "fg": btn_fg, "activebackground": highlight,
                "relief": tk.FLAT, "font": ("Arial", 10), "bd": 1, "highlightthickness": 0}

root.configure(bg=bg_color)

# Draw grid
def draw_grid(spacing=25):
    axes_drawer.color("#444444")
    for x in range(-350, 351, spacing):
        axes_drawer.penup()
        axes_drawer.goto(x, -350)
        axes_drawer.pendown()
        axes_drawer.goto(x, 350)
    for y in range(-350, 351, spacing):
        axes_drawer.penup()
        axes_drawer.goto(-350, y)
        axes_drawer.pendown()
        axes_drawer.goto(350, y)

# Draw axes and labels
def draw_axes():
    axes_drawer.color("#ffffff")
    axes_drawer.penup()
    axes_drawer.goto(-350, 0)
    axes_drawer.pendown()
    axes_drawer.goto(350, 0)
    axes_drawer.penup()
    axes_drawer.goto(-330, 5)
    axes_drawer.write("X", align="left", font=("Arial", 12, "bold"))

    axes_drawer.penup()
    axes_drawer.goto(0, -350)
    axes_drawer.pendown()
    axes_drawer.goto(0, 350)
    axes_drawer.penup()
    axes_drawer.goto(10, 270)
    axes_drawer.write("Y", align="left", font=("Arial", 12, "bold"))

    scale = 25
    for i in range(1, 14):
        axes_drawer.penup()
        axes_drawer.goto(i * scale, 5)
        axes_drawer.write(str(i), align="center", font=("Arial", 8))
        axes_drawer.goto(-i * scale, -18)
        axes_drawer.write(str(-i), align="center", font=("Arial", 8))
        axes_drawer.goto(-15, i * scale - 6)
        axes_drawer.write(str(i), align="left", font=("Arial", 8))
        axes_drawer.goto(10, -i * scale - 6)
        axes_drawer.write(str(-i), align="left", font=("Arial", 8))

    turtle.tracer(1)

# Draw polygon
def draw_polygon(pts, color="#00ffff"):
    if len(pts) < 3:
        return
    drawer.color(color)
    drawer.penup()
    drawer.goto(pts[0])
    drawer.pendown()
    for p in pts[1:]:
        drawer.goto(p)
    drawer.goto(pts[0])
    drawer.penup()

# Free-axis reflection (y = x)
def reflect_polygon_free(polygon):
    matrix = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    poly_3d = np.vstack((np.array(polygon).T, np.ones((1, len(polygon)))))
    reflected_3d = matrix @ poly_3d
    return reflected_3d[:2].T.tolist()

# Add point by click
def on_click(x, y):
    if snap_to_grid.get():
        x = round(x / 25) * 25
        y = round(y / 25) * 25
    vertices.append([x, y])
    drawer.goto(x, y)
    drawer.dot(5, "#00ffff")

# Draw polygon
def on_draw():
    drawer.clear()
    draw_polygon(vertices, "#00ffff")

# Reflect mode
def on_reflect():
    if len(vertices) < 3:
        return
    on_draw()
    mode = reflection_mode.get()
    poly = np.vstack((np.array(vertices).T, np.ones((1, len(vertices)))))
    if mode == "x":
        matrix = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
        reflected = matrix @ poly
        draw_polygon(reflected[:2].T.tolist(), "#ff4444")
    elif mode == "y":
        matrix = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
        reflected = matrix @ poly
        draw_polygon(reflected[:2].T.tolist(), "#ff4444")
    else:
        draw_polygon(reflect_polygon_free(vertices), "#ff4444")

# Clear
def on_clear():
    drawer.clear()
    axes_drawer.clear()
    vertices.clear()
    draw_grid()
    draw_axes()

# Popup to add a point
def add_point_popup():
    popup = tk.Toplevel(bg=bg_color)
    popup.title("Add Point")
    tk.Label(popup, text="X Coordinate:", **label_style).grid(row=0, column=0, padx=10, pady=5)
    x_entry = tk.Entry(popup, **entry_style)
    x_entry.grid(row=0, column=1, padx=10, pady=5)
    tk.Label(popup, text="Y Coordinate:", **label_style).grid(row=1, column=0, padx=10, pady=5)
    y_entry = tk.Entry(popup, **entry_style)
    y_entry.grid(row=1, column=1, padx=10, pady=5)

    def submit():
        try:
            x = float(x_entry.get()) * 25
            y = float(y_entry.get()) * 25
            if snap_to_grid.get():
                x = round(x / 25) * 25
                y = round(y / 25) * 25
            vertices.append([x, y])
            drawer.goto(x, y)
            drawer.dot(5, "#00ffff")
            popup.destroy()
        except:
            msgbox.showerror("Invalid Input", "Please enter valid coordinates.")

    tk.Button(popup, text="Add", command=submit, **button_style).grid(row=2, column=0, columnspan=2, pady=10)

# Create the bottom frame UI
frame = tk.Frame(root, bg=bg_color)
frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

tk.Label(frame, text="Reflection Mode:", font=("Arial", 10, "bold"),
         bg=bg_color, fg=fg_color).pack(pady=(5, 0))

radio_frame = tk.Frame(frame, bg=bg_color)
radio_frame.pack(pady=5)

for text, val in [("Free-Axis (y = x)", "free"), ("X-Axis", "x"), ("Y-Axis", "y")]:
    tk.Radiobutton(radio_frame, text=text, variable=reflection_mode, value=val,
                   bg=bg_color, fg=fg_color, selectcolor=highlight,
                   activebackground=highlight, activeforeground=fg_color,
                   font=("Arial", 10, "bold"), indicatoron=0, bd=0, relief=tk.FLAT,
                   highlightthickness=1, width=18, pady=6).pack(side=tk.LEFT, padx=6)

# Control buttons
btn_frame = tk.Frame(frame, bg=bg_color)
btn_frame.pack(pady=5)

for text, command in [
    ("Add Point", add_point_popup),
    ("Draw (D)", on_draw),
    ("Reflect (R)", on_reflect),
    ("Clear (C)", on_clear)
]:
    b = tk.Button(btn_frame, text=text, command=command, **button_style)
    b.pack(side=tk.LEFT, padx=6, pady=2)
    b.configure(cursor="hand2", highlightbackground=highlight)

# Snap to Grid checkbox
tk.Checkbutton(frame, text="Auto Snap", variable=snap_to_grid,
               bg=bg_color, fg=fg_color, selectcolor=highlight,
               activebackground=highlight, activeforeground=fg_color,
               font=("Arial", 10)).pack()

# Bind keyboard and mouse
screen.onclick(on_click)
screen.listen()
screen.onkey(on_draw, "d")
screen.onkey(on_reflect, "r")
screen.onkey(on_clear, "c")

# Initial drawing
draw_grid()
draw_axes()

# Start main loop
turtle.done()
