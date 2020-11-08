from tkinter import *
import blochat.quantum as q
import socket
import sys
import _thread
if sys.platform.startswith("linux"):
  import playsound
else:
  import winsound
import select

serverName = ""
name = ""
nameField = None
listbox = None
userInput = ""

def openChatWindow():
  global serverName
  global listbox
  global chatbox
  chatWindow = Toplevel(window)
  chatWindow.title(serverName)
  chatWindow.configure(background='#1D3557')
  scrollbar = Scrollbar(chatWindow)
  scrollbar.pack(side=RIGHT, fill=Y)
  listbox = Listbox(chatWindow, yscrollcommand=scrollbar.set)
  listbox.insert(END, "Welcome To The Chat")
  '''listbox.pack(side=LEFT, fill=X)'''
  listbox.place(x=50,y=0)
  scrollbar.config(command=listbox.yview)
  chatbox = Entry(chatWindow, width=20, bg=tBg)
  chatbox.place(x=50,y=180)
  Button(
  chatWindow, text="Enter", width=8, command=getUserMessage).place(x=80,y=220)
  chatWindow.geometry("275x250")
def openNameWindow():
  global serverName
  global nameField
  global nameWindow
  nameWindow = Toplevel(window)
  nameWindow.title("Name")
  nameWindow.configure(background='#1D3557')
  nameField = Entry(nameWindow, width=40, bg=tBg)
  Label(nameWindow, text="Enter Your Name", bg="#1D3557", fg='white', font="none 14 bold") .grid(row=0, column=0, sticky=N)
  nameField.grid(row=1, column=0, sticky=E)
  Button(
  nameWindow, text="Enter", width=8, command=nameSelect).grid(
  row=1, column=1, sticky=W)
  

def nameSelect():
  global nameField
  global name
  name = nameField.get()
  openChatWindow()
  nameWindow.destroy()
  serverLoop()
  

global server

def click():
    global serverName
    global name
    global server
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
def serverLoop():
    global server
    while True:
      sockets = [None, server]
      readS, writeS, errS = select.select(sockets,[],[])
      for Socket in readS:
        if Socket == server:
          msg = Socket.recv(2048)
          if first:
            first = False
            serverName = msg[msg.find(":") + 1:]
            server.sendall(f"/name {name}")
          msg = Socket.recv(2048)
          outputMessage(msg)
        
def awaitInput(msg):
    global server
    if True:
          print('test')
          if msg.startswith("/help"):
              outputMessage("> [ SYS.local ]: Command List:\n/help: Brings up this message.\n/circuit [-c {circuit name} {# of qubits in circuit}] [-g [X, h, z] {circuit name}] [-l]")
              return
          sMsg = msg.split()
          if len(sMsg) > 1:
              if msg.startswith("/circuit"):
                  if sMsg[1] == "-c":
                    q.circuitList[sMsg[1]] = q.QuantumCircuit(int(sMsg[2]))
                  elif sMsg[1] == "-g":
                      if sMsg[2].upper() == 'X':
                        q.circuitList[sMsg[3]] = q.circuitList[sMsg[3]].x
                      elif sMsg[2].lower() == 'h':
                        q.circuitList[sMsg[3]] = q.circuitList[sMsg[3]].h
                      elif sMsg[2].lower() == 'z':
                        q.circuitList[sMsg[3]] = q.circuitList[sMsg[3]].z
                      return
                  elif sMsg[1] == "-l":
                      catCircuit = ''
                      for i in q.circuitList:
                          catCircuit += i
                      outputMessage(f"> [ SYS.local ]: {catCircuit}")
          QMsg = q.toBinary(msg)
          messageCircuit = []
          for i in range(len(q.sep(2, QMsg))):
              messageCircuit.append(q.QuantumCircuit(2))
              q.bellPair(messageCircuit[i], 0, 1)
              q.encrypt(messageCircuit[i], 0, q.sep(2, QMsg)[i])
          server.sendall(bytearray(messageCircuit))
          outputMessage(f"> [ YOU ]: {msg}")


def launchserver():
  import blochat.server
def outputMessage(msg):
  listbox.insert(END, msg) 
def getUserMessage():
  global userInput
  userInput = chatbox.get()
  awaitInput(userInput)

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

