"""" /*
      * Program by Gian Brar and Justin Brouwer
      * hackPHS 2020
      * Tested on Windows 10 and GNU/Linux
      */ """

import sys
import blochat.server as server
from blochat.visual import *

"""" QUBIT STATES GUIDE:
     .cx(x,y) = x XOR/CNOT y
"""

if len(sys.argv) > 1:
  if sys.argv[1] == "-s" or sys.argv[1] == "--server":
    server.runServer()
    server.conn.close()
    server.server.close()
    exit()
  elif not (sys.argv[1] == "-u" or sys.argv[1] == "--user"):
    print("Ignoring unrecognized flag...")

window.mainloop()
