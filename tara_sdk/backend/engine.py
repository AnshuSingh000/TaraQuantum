from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

class QiskitEngine:
    def __init__(self):
        self.simulator = AerSimulator()

    def compile(self, tokens):
        # Determine number of qubits needed
        max_qubit = 0
        for t in tokens:
            if t.type in ['H', 'X', 'Z', 'S', 'T']:
                max_qubit = max(max_qubit, t.value['target'])
            elif t.type == 'CX':
                max_qubit = max(max_qubit, t.value['ctrl'], t.value['target'])
        
        qc = QuantumCircuit(max_qubit + 1)

        for t in tokens:
            if t.type == 'H': qc.h(t.value['target'])
            elif t.type == 'X': qc.x(t.value['target'])
            elif t.type == 'Z': qc.z(t.value['target'])
            elif t.type == 'S': qc.s(t.value['target'])
            elif t.type == 'T': qc.t(t.value['target'])
            elif t.type == 'CX': qc.cx(t.value['ctrl'], t.value['target'])
            elif t.type == 'MEASURE': qc.measure_all()
            
        return qc

    def run_simulation(self, qc):
        # Ensure measurements exist for simulation
        if not qc.cregs:
            qc.measure_all()
        job = self.simulator.run(qc, shots=1024)
        return job.result().get_counts()

    def save_diagram(self, qc, filename):
        qc.draw('mpl').savefig(filename)