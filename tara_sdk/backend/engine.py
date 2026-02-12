from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from ..utils.logger import setup_logger

log = setup_logger("BACKEND")

class QiskitEngine:
    def __init__(self):
        self.simulator = AerSimulator()

    def compile(self, tokens):
        log.info("Initializing Quantum Circuit...")
        
        # Determine number of qubits
        num_qubits = 0
        for t in tokens:
            if t.type == 'CREATE':
                num_qubits = t.value
                break
        
        qc = QuantumCircuit(num_qubits)
        
        for t in tokens:
            if t.type == 'H':
                qc.h(t.value['target'])
            elif t.type == 'X':
                qc.x(t.value['target'])
            elif t.type == 'Z':
                qc.z(t.value['target'])
            # --- NEW PHASE GATES ---
            elif t.type == 'S':
                qc.s(t.value['target'])
                log.info(f"Applied S gate (90 deg) to qubit {t.value['target']}")
            elif t.type == 'T':
                qc.t(t.value['target'])
                log.info(f"Applied T gate (45 deg) to qubit {t.value['target']}")
            # -----------------------
            elif t.type == 'CX':
                qc.cx(t.value['ctrl'], t.value['target'])
            elif t.type == 'ENTANGLE':
                q1, q2 = t.value['q1'], t.value['q2']
                qc.h(q1)
                qc.cx(q1, q2)
                log.info(f"Macro expanded: Entangled {q1} and {q2}")
            elif t.type == 'MEASURE':
                qc.measure_all()
                
        return qc

    def run_simulation(self, qc, shots=1024):
        log.info(f"Simulating circuit with {shots} shots...")
        compiled_circuit = transpile(qc, self.simulator)
        result = self.simulator.run(compiled_circuit, shots=shots).result()
        counts = result.get_counts()
        log.info(f"Simulation Results: {counts}")
        return counts

    def save_diagram(self, qc, filename="tara_circuit.png"):
        log.info(f"Rendering blueprint to {filename}...")
        fig = qc.draw(output='mpl', style='iqp')
        fig.savefig(filename, dpi=300)
        plt.close()