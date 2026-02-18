class QInspector:
    def __init__(self):
        self.max_depth = 10  # Max gates allowed before decoherence risk
        
    def analyze(self, tokens):
        report = {
            "gate_count": 0,
            "qubits_used": set(),
            "warnings": [],
            "health_score": 100
        }
        
        measured_qubits = set()
        
        for t in tokens:
            if t.type != 'CREATE':
                report["gate_count"] += 1
            
            # 1. Check for Gate-After-Measure (The Zombie Gate)
            if t.type in ['SPIN', 'X', 'Z', 'LINK']:
                target = t.value.get('target')
                if target in measured_qubits:
                    report["warnings"].append(f"CRITICAL: Attempted gate on Qubit {target} after OBSERVE.")
                    report["health_score"] -= 30
            
            if t.type == 'OBSERVE':
                # For simplicity, assume all are measured
                measured_qubits.add(0) # Logic expansion needed for specific qubits
                
        # 2. Check Depth (Decoherence Risk)
        if report["gate_count"] > self.max_depth:
            report["warnings"].append(f"WARNING: Circuit depth ({report['gate_count']}) exceeds coherence limits.")
            report["health_score"] -= 20

        return report