"""" /*
      * Program by Gian Brar and Justin Brouwer
      * hackPHS 2020
      * Tested on Windows 10 and GNU/Linux
      */ """

import sys
from blochat.visual import *

"""" QUBIT STATES GUIDE:
     .cx(x,y) = x XOR/CNOT y
"""

if len(sys.argv) > 1:
  if sys.argv[1] == "-s" or sys.argv[1] == "--server":
    import blochat.blochat.server
  elif sys.argv[1] == "-u" or sys.argv[1] == "--user":
    window.mainloop()
  else:
    print("Unrecognized flag.")
    exit()
else:
  window.mainloop()
