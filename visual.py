from tkinter import *

entered_text = ""


def click():
    global entered_text
    entered_text = textbloch.get()
    print(entered_text)
    ipcheck()
def ipcheck():
  """server.py validate IP"""
  """if ip is correct:"""
  print("Checked")
  """else:"""


window = Tk()
window.title("Blochat")
window.configure(background="black")

photo1 = PhotoImage(file="IMG/blochat_icon_small.png")
Label(window, image=photo1, bg="black").grid(row=0, column=0, sticky=W)

Label(
    window, text="Blochat", bg="black", fg="white", font="none 60 bold").grid(
        row=0, column=1, sticky=S)

Label(
    window,
    text="\n\nEnter Server IP In\nThe Box Below",
    bg="black",
    fg="white",
    font="none 20 bold").grid(
        row=1, column=0, sticky=W)
textbloch = Entry(window, width=40, bg="white")
textbloch.grid(row=2, column=0, sticky=N)
Button(
    window, text="Join", width=10, command=click).grid(
        row=2, column=1, sticky=N)
window.mainloop()
