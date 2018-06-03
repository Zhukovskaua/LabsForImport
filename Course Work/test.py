from tkinter import *

f = input('f(x):')

root = Tk()

canvas = Canvas(root, width=1000, height=1000, bg="white")
canvas.create_line(500, 1000, 500, 0, width=2, arrow=LAST)
canvas.create_line(0, 500, 1000, 500, width=2, arrow=LAST)
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))
First_x = -500

for i in range(16000):
    if i % 800 == 0:
        k = First_x + (1 / 16) * i
        canvas.create_line(k + 500, -3 + 500, k + 500, 3 + 500, width=0.5, fill='black')
        canvas.create_text(k + 515, -10 + 500, text=str(k), fill="purple", font=("Helvectica", "10"))
        if k != 0:
            canvas.create_line(-3 + 500, k + 500, 3 + 500, k + 500, width=0.5, fill='black')
            canvas.create_text(20 + 500, -k + 500, text=str(k), fill="purple", font=("Helvectica", "10"))
    try:
        x = First_x + (1 / 16) * i
        new_f = f.replace('x', str(x))
        y = -eval(new_f) + 500
        x += 500
        canvas.create_oval(x, y, x + 1, y + 1, fill='black')
    finally:
        pass
canvas.pack()
root.mainloop()
