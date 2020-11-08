import socket
import _thread
import blochat.quantum
from requests import get

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = ""
clients = []

print("> Blochat Server Client activated.")
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 0

name = input("> Create server name\n> ")
if not name:
  name = socket.gethostname()
port = input("> Enter port #\n> ")
wl = input("> Use link (l) or IP (i)? [default i]\n> ")
if wl.lower() == 'l':
    try:
        url = socket.gethostbyname(input("> Enter URL ('www.google.com' format)\n> "))
    except:
        print("ERROR: Host resolution failed.")
        exit()
else:
    ie = input("> Form IPv4 (i) or IPv6 (e) connection? [default i]\n> ")
    if ie.lower() == 'e':
        sIP = get("https://api.ipify.org").text
    else:
        sIP = socket.gethostbyname(socket.gethostname())
print(f"IP detected as {sIP}")
    
try:
  server.bind((sIP, int(port)))
except:
  print("ERROR: Faulty hostname and/or port.")
  exit()

server.listen(10) # arbitrary number; change at any time
def clientThread(conn, addr):
  global clients
  global name
  conn.send(bytes(f"Entered chatroom: {name}", "utf-8"))
  first = True
  uname = addr[0]
  while True:
    try:
      message = conn.recv(2048)
      formatMsg = ''
      if message != '':
        if len(message.split()) > 1:
            if message.startswith("/name"):
                name = message.split()[1]
        if first:
            first = False
            formatMsg = f"> {uname} joined the server."
        else:
            formatMsg = f"> [ {uname} ]: {message}"
        print(formatMsg)
      for client in clients:
        if client != conn:
          try:
            client.send(formatMsg)
          except:
            client.close()
            clients.remove(client)
            conn.send(bytes(f"> {uname} left the server.", "utf-8"))
    except:
      continue

while True:
  conn, addr = server.accept()
  clients.append(conn)
  _thread.start_new_thread(clientThread(conn, addr))

conn.close()
server.close()
