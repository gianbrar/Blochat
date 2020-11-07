import socket
import _thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = ""
clients = []

print("> Blochat Server Client activated.")
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 0

name = input("> Create server name\n> ")
if name == "":
  name = socket.gethostname()
port = input("> Enter port #\n> ")

print(f"IP detected as {socket.gethostbyname(socket.gethostname())}")

try:
  server.bind((socket.gethostbyname(socket.gethostname()), int(port)))
except:
  print("ERROR: Faulty hostname and/or port.")
  exit()

server.listen(10)
def clientThread(conn, addr):
  global clients
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

while True:
  conn, addr = server.accept()
  clients.append(conn)
  print(f"{addr[0]} joined the server.")
  _thread.start_new_thread(clientThread(conn, addr))

conn.close()
server.close()