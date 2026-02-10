from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
from ..utils.logger import setup_logger

log = setup_logger("BACKEND")

class QiskitEngine:
    def compile(self, tokens):
        log.info("Initializing Quantum Circuit...")
        num_qubits = tokens[0].value
        qc = QuantumCircuit(num_qubits)
        
        for t in tokens:
            if t.type == 'H':
                qc.h(t.value['target'])
            elif t.type == 'CX':
                qc.cx(t.value['ctrl'], t.value['target'])
            elif t.type == 'MEASURE':
                qc.measure_all()
                
        return qc

    def save_diagram(self, qc, filename="circuit.png"):
        log.info(f"Rendering blueprint to {filename}...")
        qc.draw(output='mpl', style='iqp').savefig(filename, dpi=300)