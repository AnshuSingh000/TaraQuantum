from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
# This import links the Engine to the Lexer's definition of a Token
from tara_sdk.core.lexer import Token 

class QiskitEngine:
    def __init__(self):
        self.simulator = AerSimulator()

    def compile(self, tokens):
        # Pass 1: Determine qubit requirements
        max_q = 0
        for t in tokens:
            if t.type == 'CREATE': 
                max_q = max(max_q, t.value)
            elif isinstance(t.value, dict):
                vals = [v for v in t.value.values() if isinstance(v, int)]
                if vals: max_q = max(max_q, max(vals) + 1)
        
        qc = QuantumCircuit(max(max_q, 1))

        # Pass 2: Map T.A.R.A. commands to Qiskit gates
        for t in tokens:
            if t.type in ['H', 'SPIN']: 
                qc.h(t.value['target'])
            elif t.type == 'X': 
                qc.x(t.value['target'])
            elif t.type == 'Z': 
                qc.z(t.value['target'])
            elif t.type in ['LINK', 'ENTANGLE']: 
                qc.cx(t.value['ctrl'], t.value['target'])
            elif t.type in ['MEASURE', 'OBSERVE']: 
                qc.measure_all()
            
        return qc

    def run_locally(self, qc):
        # Local simulation for privacy and speed
        if not qc.cregs: 
            qc.measure_all()
        
        job = self.simulator.run(qc, shots=1024)
        return job.result().get_counts()

    def save_vision(self, qc, filename="tara_circuit.png"):
        # Generates the visual quantum circuit diagram
        fig = qc.draw('mpl')
        fig.savefig(filename)
        plt.close(fig)