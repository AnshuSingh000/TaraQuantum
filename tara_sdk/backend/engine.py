from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

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
                if vals: max_q = max(max_q, max(vals))
        
        # Ensure we have at least one qubit
        qc = QuantumCircuit(max(max_q + 1, 1))

        # Pass 2: Map T.A.R.A. commands to Qiskit gates
        for t in tokens:
            if t.type in ['H', 'SPIN', 'HADAMARD']: 
                qc.h(t.value['target'])
            elif t.type == 'X': 
                qc.x(t.value['target'])
            elif t.type == 'Z': 
                qc.z(t.value['target'])
            elif t.type in ['LINK', 'ENTANGLE', 'CNOT']: 
                qc.cx(t.value['ctrl'] if 'ctrl' in t.value else t.value.get('control', 0), 
                      t.value['target'])
            elif t.type in ['MEASURE', 'OBSERVE']: 
                qc.measure_all()
            
        return qc

    def run_locally(self, qc):
        # Automatic measurement if the user forgot
        if not qc.cregs: 
            qc.measure_all()
        
        # Using 512 shots to show clear quantum variance for the demo
        compiled_circuit = transpile(qc, self.simulator)
        job = self.simulator.run(compiled_circuit, shots=512)
        return job.result().get_counts()

    def save_vision(self, qc, filename="tara_circuit.png"):
        # Generates the visual quantum circuit diagram
        # 
        fig = qc.draw('mpl')
        fig.savefig(filename)
        plt.close(fig)