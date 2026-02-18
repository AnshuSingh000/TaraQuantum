from ..utils.logger import setup_logger

log = setup_logger("INSPECTOR")

class Inspector:
    def analyze(self, tokens):
        log.info("Running Static Analysis (Safety Check)...")
        errors = []
        max_qubits = 0
        
        # Pass 1: Find System Size
        for t in tokens:
            if t.type == 'CREATE':
                max_qubits = t.value
                break
        
        if max_qubits == 0:
            return False, ["FATAL: No 'Create qubits' command found."]

        # Pass 2: Check Logic
        for t in tokens:
            if t.type == 'H':
                q = t.value['target']
                if q >= max_qubits:
                    errors.append(f"Line {t.line}: Logic Error! Qubit {q} does not exist (Max: {max_qubits-1}).")
            
            if t.type == 'CX':
                c, tgt = t.value['ctrl'], t.value['target']
                if c == tgt:
                    errors.append(f"Line {t.line}: Physics Violation! Cannot entangle Qubit {c} with itself.")

        if errors:
            log.error(f"Found {len(errors)} critical errors.")
            return False, errors
            
        log.info("✅ Code is clean. Proceeding to compilation.")
        return True, []