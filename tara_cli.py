import sys
import os

# Adds the current directory to the system path so Python finds 'tara_sdk'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from tara_sdk.core.lexer import Lexer
    from tara_sdk.backend.engine import QiskitEngine
    from tara_sdk.utils.visualizer import print_histogram
    from tara_sdk.utils.voice import TaraVoice
except ImportError as e:
    print(f"❌ Setup Error: {e}")
    sys.exit(1)

def run_tara(file_name):
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
        tokens = lexer.tokenize(code)
        qc = engine.compile(tokens)
        
        # Execution
        results = engine.run_locally(qc) 
        print_histogram(results)
        
        # Save Visualization
        engine.save_vision(qc, "tara_circuit.png")
        voice.speak("Execution complete.")
        
    except Exception as e:
        print(f"⚠️ Error: {e}")
        voice.speak("A logic error occurred.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_tara(sys.argv[1])
    else:
        print("Usage: python tara_cli.py bell_test.tara")