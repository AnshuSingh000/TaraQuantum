import sys
import os

# Ensure we can find the tara_sdk folder
sys.path.append(os.getcwd())

from tara_sdk.core.lexer import Lexer
from tara_sdk.analysis.inspector import Inspector
from tara_sdk.backend.engine import QiskitEngine
from tara_sdk.utils.voice import TaraVoice  # <--- NEW IMPORT

def main():
    # 1. Initialize the Voice
    voice = TaraVoice()
    
    # 2. Greeting
    voice.speak("Tara System Online. Awaiting Quantum Instructions.")

    # 3. Initialize the Brain
    lexer = Lexer()
    inspector = Inspector()
    engine = QiskitEngine()
    
    code_buffer = []

    print("==========================================")
    print("   T.A.R.A. Quantum Compiler (v1.1)       ")
    print("==========================================")

    while True:
        try:
            line = input("   > ").strip()
        except KeyboardInterrupt:
            voice.speak("Shutting down.")
            break
            
        # HANDLE EXIT
        if line.lower() in ["exit", "quit"]:
            voice.speak("Goodbye, Commander.")
            break
            
        # HANDLE RUN
        if line.lower() == "run":
            if not code_buffer:
                voice.speak("Buffer is empty. Please add commands first.")
                continue

            voice.speak("Compiling circuit...")
            full_script = "\n".join(code_buffer)
            
            # --- LEXER ---
            tokens = lexer.tokenize(full_script)
            
            # --- INSPECTOR ---
            is_safe, errors = inspector.analyze(tokens)
            if not is_safe:
                voice.speak("Safety protocol violated.")
                for err in errors:
                    print(f"❌ {err}")
                code_buffer = []
                continue

            # --- ENGINE ---
            try:
                qc = engine.compile(tokens)
                print(qc) # Print ASCII art
                
                # Save the image
                engine.save_diagram(qc, "tara_circuit.png")
                
                voice.speak("Circuit generated successfully.")
                
            except Exception as e:
                voice.speak("System error detected.")
                print(e)
            
            # Clear buffer for next run
            code_buffer = []
        
        # HANDLE REGULAR COMMANDS
        else:
            if line:
                code_buffer.append(line)

if __name__ == "__main__":
    main()