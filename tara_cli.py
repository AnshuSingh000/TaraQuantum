from tara_sdk.core.lexer import Lexer
from tara_sdk.analysis.inspector import Inspector
from tara_sdk.backend.engine import QiskitEngine

def main():
    print("\n--- T.A.R.A. ENTERPRISE v4.0 ---")
    
    # 1. The Script (INTENTIONALLY BROKEN)
    script = """
    Create 2 qubits
    Superpose qubit 0
    Link 0 to 0     
    Flip qubit 5    
    Measure all
    """
    
    # 2. The Pipeline
    tokens = Lexer().tokenize(script)
    is_safe, errors = Inspector().analyze(tokens)
    
    if is_safe:
        circuit = QiskitEngine().compile(tokens)
        QiskitEngine().save_diagram(circuit, "enterprise_circuit.png")
        print("\n[SUCCESS] Pipeline Completed. Artifact generated.")
    else:
        print("\n[FAILED] Safety Protocols Triggered:")
        for e in errors: 
            print(f"❌ {e}")

if __name__ == "__main__":
    main()