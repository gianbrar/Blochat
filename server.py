import socket
import sys

print("> Blochat Server Client activated.")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
port = 0

if len(sys.argv > 1):
  int(sys.argv[1])
else:
  input("> Enter port #\n> ")

server.bind((socket.gethostname(), port))
