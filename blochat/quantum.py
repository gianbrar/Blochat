from qiskit import *

circuitList = {}

def bellPair(circuit, x, y):
    circuit.h(x)
    circuit.cx(x, y)
            
def encrypt(circuit, qbit, bits):
    if msg == "10":
        circuit.x(qbit)
    elif msg == "01":
        circuit.z(qbit)
    elif msg == "11":
        circuit.z(qubit)
        circuit.x(qubit)
    else:
        pass

def decrypt(circuit, x, y):
    circuit.cx(x, y)
    circuit.h(x)

def sep(x, sepStr):
    return [sepStr[i:i+x] for i in range (0, len(sepStr), x)]

def bToStr(bstr):
    returnStr = ''
    for b in ' '.join(sep(8, bstr)).split():
        returnStr += chr(int(b, 2))
    return returnStr

def toBinary(bstr):
    return ''.join(format(ord(x), 'b') for x in bstr)
