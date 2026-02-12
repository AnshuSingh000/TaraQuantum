import os
import platform # Added to detect the operating system
from tara_sdk.core.lexer import Lexer
from tara_sdk.backend.engine import QiskitEngine

def speak(text):
    """Detects the OS and uses the native voice engine."""
    current_os = platform.system()
    try:
        if current_os == "Darwin":  # macOS
            os.system(f"say '{text}' &")
        elif current_os == "Windows":
            # Uses PowerShell's speech engine
            ps_cmd = f'Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak("{text}")'
            os.system(f'powershell -Command "{ps_cmd}" &')
        elif current_os == "Linux":
            # Uses espeak (standard on most Linux distros)
            os.system(f"espeak '{text}' &")
    except Exception:
        # Fallback if audio drivers are missing
        pass

def main():
    print("-" * 50)
    print("T.A.R.A. v1.2 - Universal Quantum Compiler")
    print("Type 'run' to execute or 'exit' to quit.")
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
            
            if line.lower() == 'run':
                if not code_buffer:
                    print("Error: No commands to run.")
                    continue
                
                print("Processing instructions...")
                
                # 1. Convert English to Tokens
                full_code = "\n".join(code_buffer)
                tokens = lexer.tokenize(full_code)
                
                # 2. Build the Quantum Circuit
                qc = engine.compile(tokens)
                print("✓ Circuit generated successfully.")
                
                # 3. Save the Blueprint
                engine.save_diagram(qc, "tara_circuit.png")
                print("✓ Blueprint saved to tara_circuit.png")
                
                # 4. Run the Physics Simulation
                print("✓ Running simulation on Aer Simulator...")
                counts = engine.run_simulation(qc)
                
                # 5. Show Results & Speak
                print("\n" + "="*30)
                print(f"SIMULATION RESULTS: {counts}")
                print("="*30 + "\n")
                
                speak("Simulation complete.")
                
                code_buffer = [] 
            else:
                code_buffer.append(line)
                
        except Exception as e:
            print(f"\n[ERROR]: {e}")
            speak("System error detected.")

if __name__ == "__main__":
    main()