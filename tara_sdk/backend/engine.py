from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
from ..utils.logger import setup_logger

log = setup_logger("BACKEND")

class QiskitEngine:
    def compile(self, tokens):
        log.info("Initializing Quantum Circuit...")
        
        # Determine number of qubits from the first CREATE token
        num_qubits = 0
        for t in tokens:
            if t.type == 'CREATE':
                num_qubits = t.value
                break
        
        qc = QuantumCircuit(num_qubits)
        
        for t in tokens:
            # 1. Hadamard Gate (Superposition)
            if t.type == 'H':
                qc.h(t.value['target'])
            
            # 2. X-Gate (The "Quantum NOT") <--- NEW
            elif t.type == 'X':
                qc.x(t.value['target'])

            # 3. Z-Gate (The "Phase Flip") <--- NEW
            elif t.type == 'Z':
                qc.z(t.value['target'])

            # 4. CNOT Gate (Entanglement)
            elif t.type == 'CX':
                qc.cx(t.value['ctrl'], t.value['target'])
            
            # 5. Measure
            elif t.type == 'MEASURE':
                qc.measure_all()
                
        return qc

    def save_diagram(self, qc, filename="circuit.png"):
        log.info(f"Rendering blueprint to {filename}...")
        qc.draw(output='mpl', style='iqp').savefig(filename, dpi=300)