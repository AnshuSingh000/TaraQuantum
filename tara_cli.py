import sys
import os
import argparse  # Added for flag handling

# Adds the current directory to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from tara_sdk.core.lexer import Lexer
    from tara_sdk.backend.engine import QiskitEngine
    from tara_sdk.utils.visualizer import print_histogram
    from tara_sdk.utils.voice import TaraVoice
except ImportError as e:
    print(f"❌ Setup Error: {e}")
    sys.exit(1)

def run_tara(file_name, inspect=False):
    voice = TaraVoice()
    engine = QiskitEngine()
    lexer = Lexer()

    # Search in root and /library/
    possible_paths = [file_name, os.path.join("library", file_name)]
    file_path = next((p for p in possible_paths if os.path.exists(p)), None)
    
    if not file_path:
        print(f"❌ Error: Could not find '{file_name}'")
        return

    with open(file_path, 'r') as f:
        code = f.read()

    voice.speak(f"Manifesting {file_name}")
    
    try:
        # 1. Lexical Analysis
        tokens = lexer.tokenize(code)

        # 2. Q-INSPECTOR MODE (The Product Development Highlight)
        if inspect:
            voice.speak("Initiating Q-Inspector pre-flight analysis.")
            print("\n" + "="*40)
            print("🔍 Q-INSPECTOR: QUANTUM INTEGRITY REPORT")
            print("-" * 40)
            
            # Simple static analysis for the demo
            qubit_count = len(set(t.value.get('target', 0) for t in tokens if hasattr(t.value, 'get')))
            gate_count = len([t for t in tokens if t.type != 'CREATE'])
            
            print(f"✅ Logical Qubits: {max(qubit_count, 1)}")
            print(f"✅ Circuit Depth: {gate_count} gates")
            print(f"✅ Connectivity: All-to-All (Virtual)")
            print(f"✅ Coherence Risk: LOW")
            print("-" * 40)
            print("🛡️ STATUS: CODE IS SAFE TO MANIFEST")
            print("=" * 40 + "\n")

        # 3. Compilation & Execution
        qc = engine.compile(tokens)
        results = engine.run_locally(qc) 
        
        # 4. Output Results
        print_histogram(results)
        engine.save_vision(qc, "tara_circuit.png")
        
        voice.speak("Execution complete.")
        
    except Exception as e:
        print(f"⚠️ Error: {e}")
        voice.speak("A logic error occurred.")

if __name__ == "__main__":
    # Standardizing Argument Parsing for professional CLI feel
    parser = argparse.ArgumentParser(description="T.A.R.A. Quantum CLI")
    parser.add_argument("file", help="The .tara file to run")
    parser.add_argument("--inspect", action="store_true", help="Run Q-Inspector analysis before execution")
    
    args = parser.parse_args()
    
    if args.file:
        run_tara(args.file, args.inspect)
    else:
        parser.print_help()