from tkinter import *
import socket
import sys
if sys.platform.startswith("linux"):
  import playsound
else:
  import winsound
import select

serverName = ""
name = ""
nameField = None

def openNameWindow():
  global serverName
  global nameField
  nameWindow = Toplevel(window)
  nameWindow.title(serverName)
  nameWindow.configure(background='#1D3557')
  nameField = Entry(nameWindow, width=40, bg=tBg)
  Label(nameWindow, text="Enter Your Name", bg="#1D3557", fg='white', font="none 14 bold") .grid(row=0, column=0, sticky=N)
  nameField.grid(row=1, column=0, sticky=E)
  Button(
  nameWindow, text="Enter", width=8, command=nameSelect).grid(
  row=1, column=1, sticky=W)
      
def nameSelect():
  global nameField
  name = nameField.get()
  print(name)

def click():
    global serverName
    server_ip = textbloch.get()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if server_ip.find(':') == -1 or len(server_ip) - 1 == server_ip.find(':'):
      invalidip()
      return
    server_port = int(server_ip[server_ip.find(':') + 1:])
    try:
        server.connect((server_ip[:server_ip.find(':')], server_port))
    except:
      invalidip()
      return
    first = True
    openNameWindow()
    while True:
      sockets = [None, server]
      readS, writeS, errS = select.select(sockets,[],[])
      for Socket in readS:
        if Socket == server:
          msg = Socket.recv(2048)
          if first:
            first = False
            serverName = msg[msg.find(":") + 1:]
            server.send(""
          msg = Socket.recv(2048) 
          outputMessage(msg)
        else:
          msg = getUserMessage()
          server.send(msg)
          outputMessage("> [ YOU ]: " + msg)


def launchserver():
  import blochat.server

def outputMessage(msg):
  print("test")

def getUserMessage():
  print("test")

window = Tk()
window.title("Blochat")
window.configure(background='#1D3557')
def invalidip():
  Label(
    window,
    text="Invalid IP or Port",
    bg="#1D3557",
    fg="red",
    font="none 14 bold").grid(
        row=4, column=0, sticky=N)
  if sys.platform.startswith("linux"):
    playsound.playsound("CTX/err.wav")
  else:
    winsound.PlaySound("CTX/err.wav", winsound.SND_FILENAME)
Button(
    window, text="Server Mode", width=10, command=launchserver).grid(
        row=0, column=10, sticky=W)
Button(
    window, text="Dev Mode", width=10, command=openNameWindow).grid(
        row=0, column=0, sticky=W)
photo1 = PhotoImage(file="CTX/blochat_icon_small.png")
Label(window, image=photo1, bg="#1D3557").grid(row=1, column=0, sticky=W)

Label(
    window, text="Blochat", bg="#1D3557", fg="white", font="none 60 bold").grid(
        row=1, column=1, sticky=S)

Label(
    window,
    text="\n\nEnter Server IP In\nThe Box Below",
    bg="#1D3557",
    fg="white",
    font="none 20 bold").grid(
        row=2, column=0, sticky=N)

tBg = ""
if sys.platform.startswith("linux"):
  tBg = "#457B9D"
else:
  tBg = "#A8DADC"

textbloch = Entry(window, width=40, bg=tBg)
textbloch.grid(row=3, column=0, sticky=N)
Button(
    window, text="Join", width=10, command=click).grid(
        row=3, column=1, sticky=W)

