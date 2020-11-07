from tkinter import *
import socket


def click():
    server_ip = textbloch.get()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if server_ip.indexOf(':') == -1 or server_ip.length() - 1 == server_ip.indexOf(':'):
      invalidip("No port found.")
    server_port = int(server_ip[server_ip.indexOf(':') + 1:])
    try:
      server.connect((server_ip, server_port))
    except:
      invalidip("ERROR: Faulty hostname and/or port.")

def launchserver():
  import blochat.server



window = Tk()
window.title("Blochat")
window.configure(background="black")
def invalidip(err):
  Label(
    window,
    text=err,
    bg="black",
    fg="red",
    font="none 14 bold").grid(
        row=4, column=0, sticky=N)
Button(
    window, text="Server Mode", width=10, command=launchserver).grid(
        row=0, column=10, sticky=W)
photo1 = PhotoImage(file="CTX/blochat_icon_small.png")
Label(window, image=photo1, bg="black").grid(row=1, column=0, sticky=W)

Label(
    window, text="Blochat", bg="black", fg="white", font="none 60 bold").grid(
        row=1, column=1, sticky=S)

Label(
    window,
    text="\n\nEnter Server IP In\nThe Box Below",
    bg="black",
    fg="white",
    font="none 20 bold").grid(
        row=2, column=0, sticky=N)

tBg = ""
if sys.platform.startswith("linux"):
  tBg = "black"
else:
  tBg = "white"

textbloch = Entry(window, width=40, bg=tBg)
textbloch.grid(row=3, column=0, sticky=N)
Button(
    window, text="Join", width=10, command=click).grid(
        row=3, column=1, sticky=W)
