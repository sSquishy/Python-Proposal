from tkinter import *

top = Tk()
top.geometry("700x350")

frame1 = Frame(top, highlightbackground="blue", highlightthickness=2)
frame1.pack(padx=20, pady=20)

C1 = Checkbutton(frame1, text = "Music", width=200, anchor="w")
C1.pack(padx=10, pady=10)

C2 = Checkbutton(frame1, text = "Video", width=200, anchor="w")
C2.pack(padx=10, pady=10)

C3 = Checkbutton(frame1, text = "Songs", width=200, anchor="w")
C3.pack(padx=10, pady=10)

C4 = Checkbutton(frame1, text = "Games", width=200, anchor="w")
C4.pack(padx=10, pady=10)

Button(frame1, text="Button-1", font=("Calibri",12,"bold")).pack(padx=10, pady=10)

top.mainloop()