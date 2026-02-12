import os
import platform
from tara_sdk.core.lexer import Lexer
from tara_sdk.backend.engine import QiskitEngine

def speak(text):
    """Detects the OS and uses the native voice engine."""
    current_os = platform.system()
    try:
        if current_os == "Darwin":  # macOS
            os.system(f"say '{text}' &")
        elif current_os == "Windows":
            ps_cmd = f'Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak("{text}")'
            os.system(f'powershell -Command "{ps_cmd}" &')
        elif current_os == "Linux":
            os.system(f"espeak '{text}' &")
    except Exception:
        pass

def main():
    print("-" * 50)
    print("T.A.R.A. v1.3 - Natural Language Quantum Compiler")
    print("Commands: 'run' to execute, 'clear' to reset, 'exit' to quit.")
    print("-" * 50)
    
    lexer = Lexer()
    engine = QiskitEngine()
    
    code_buffer = []
    
    while True:
        try:
            line = input("tara> ").strip()
            
            if not line:
                continue
                
            if line.lower() == 'exit':
                speak("Shutting down. Goodbye.")
                break

            # NEW: The Clear Command
            if line.lower() == 'clear':
                code_buffer = []
                print("✓ Buffer cleared. Ready for a new circuit.")
                speak("Memory cleared.")
                continue
            
            if line.lower() == 'run':
                if not code_buffer:
                    print("Error: No commands to run.")
                    continue
                
                print("Processing instructions...")
                
                # 1. Tokenize (Now understands synonyms like 'spin' or 'spawn')
                full_code = "\n".join(code_buffer)
                tokens = lexer.tokenize(full_code)
                
                # 2. Build
                qc = engine.compile(tokens)
                print("✓ Circuit generated successfully.")
                
                # 3. Save
                engine.save_diagram(qc, "tara_circuit.png")
                print("✓ Blueprint saved to tara_circuit.png")
                
                # 4. Simulate
                print("✓ Running simulation on Aer Simulator...")
                counts = engine.run_simulation(qc)
                
                # 5. Output
                print("\n" + "="*30)
                print(f"SIMULATION RESULTS: {counts}")
                print("="*30 + "\n")
                
                speak(f"Simulation complete. Results are {counts}")
                
                code_buffer = [] 
            else:
                # Store the input lines
                code_buffer.append(line)
                
        except Exception as e:
            print(f"\n[ERROR]: {e}")
            speak("I encountered an error.")

if __name__ == "__main__":
    main()