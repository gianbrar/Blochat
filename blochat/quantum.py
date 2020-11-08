from qiskit import *

circuitList = {}

def bellPair(circuit, x, y):
    circuit.h(x)
    circuit.cx(x, y)
            
def encrypt(circuit, qbit, bits):
    if bits == "10":
        circuit.x(qbit)
    elif bits == "01":
        circuit.z(qbit)
    elif bits == "11":
        circuit.z(qbit)
        circuit.x(qbit)
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
