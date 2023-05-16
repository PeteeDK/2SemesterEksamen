import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack()

#Check in
button = tk.Button(canvas,text="Check In")
button.place(relx=0, relheight=.2, relwidth=0.3)

#Check Out
button = tk.Button(canvas,text="Check Out")
button.place(relx=0, rely=.2, relheight=.2, relwidth=0.3)
root.mainloop()