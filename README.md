# ReflectX 📐✨

## Description
ReflectX is an interactive 2D computer graphics tool built with Python to help visualize geometric reflections. Users can dynamically plot custom shapes on a cartesian grid and instantly reflect them across the X-Axis, Y-Axis, or the Free-Axis ($y = x$) using homogeneous coordinate transformation matrices. 

---

## Project Previews

### 1. Drawing a Shape
![Draw Shape](draw.png)

### 2. X-Axis Reflection
![X-Axis Reflection](reflect%20x-axis.png)

### 3. Y-Axis Reflection
![Y-Axis Reflection](reflect%20y-axis.png)

### 4. Free-Axis (y = x) Reflection
![Free-Axis Reflection](reflect%20free-axis.png)

---

## Features
- **Click to Plot:** Left-click anywhere on the dark grid to place vertices.
- **Auto Snap:** Automatically snaps points perfectly to the nearest grid intersection (25px scale increments).
- **Matrix Engine:** Calculates real-time transformations using 3x3 homogeneous coordinate matrices.
- **Keyboard Shortcuts:** Built-in listeners for rapid canvas control.

---

## Technologies Used
* **Python 3.x**
* **Turtle Graphics** (Canvas rendering)
* **Tkinter** (Dark-themed user interface controls)
* **NumPy** (Multi-dimensional matrix multiplication engine)

---

## How to Use
1. **Add Points:** Left-click on the grid canvas to place dots, or click the **Add Point** button to enter exact coordinates manually.
2. **Draw:** Press the **D** key or click the **Draw (D)** button to connect your points into a cyan shape.
3. **Choose Mode:** Select your reflection line at the bottom control bar (**X-Axis**, **Y-Axis**, or **Free-Axis**).
4. **Reflect:** Press the **R** key or click **Reflect (R)** to instantly view the calculated transformation in red.
5. **Clear:** Press the **C** key or click **Clear (C)** to wipe the board and start fresh.

---

## Matrix Transformations
ReflectX converts 2D coordinates into a homogeneous system to execute linear algebra operations:

### X-Axis Reflection ($y = 0$)
$$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$

### Y-Axis Reflection ($x = 0$)
$$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} -1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$

### Free-Axis Reflection ($y = x$)
$$\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}$$

---

## File Structure
```text
├── CG_project.py         # Main Python source application script
├── axes.ico              # Custom window application icon
├── draw.png              # Interface preview graphic asset
├── reflect x-axis.png    # Interface preview graphic asset
├── reflect y-axis.png    # Interface preview graphic asset
└── reflect free-axis.png # Interface preview graphic asset