import socket
import sys

print("> Blochat Server Client activated.")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 0
clients = []

name = input("> Create server name\n> ")
if name == "":
  name = socket.gethostname()
if len(sys.argv > 1):
  port = int(sys.argv[1]) 
else:
  port = input("> Enter port #\n> ")

try:
  server.bind((socket.gethostname(), port))
except:
  print("ERROR: Faulty hostname and/or port.")

server.listen(10)
def clientThread(conn, addr):
  conn.send(f"Entered chatroom: {name}")
  while True:
    try:
      message = conn.recv(2048)
      formatMsg = f"> [ {addr[0]} ]: {message}"
      print(formatMsg)
      for client in clients:
        if client != conn:
          try:
            client.send(formatMsg)
          except:
            client.close()
            clients.remove(client)
    except:
      continue