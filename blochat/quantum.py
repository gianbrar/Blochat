from qiskit import *

circuitList = {}

def bellPair(circuit, x, y):
    circuit.h(x)
    circuit.cx(x, y)
