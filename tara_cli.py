import os
import platform
from tara_sdk.core.lexer import Lexer
from tara_sdk.backend.engine import QiskitEngine
from tara_sdk.utils.visualizer import print_histogram

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
    print("T.A.R.A. v1.4 - Natural Language Quantum Compiler")
    print("Commands: 'run', 'clear', 'save [name]', 'load [name]', 'exit'")
    print("-" * 50)
    
    lexer = Lexer()
    engine = QiskitEngine()
    
    code_buffer = []
    
    while True:
        try:
            line = input("tara> ").strip()
            
            if not line:
                continue
                
            cmd_lower = line.lower()

            if cmd_lower == 'exit':
                speak("Shutting down. Goodbye.")
                break

            if cmd_lower == 'clear':
                code_buffer = []
                print("✓ Buffer cleared. Ready for a new circuit.")
                speak("Memory cleared.")
                continue

            # --- NEW: SAVE LOGIC ---
            if cmd_lower.startswith('save '):
                filename = line.split(' ', 1)[1].strip()
                if not filename.endswith('.tara'):
                    filename += '.tara'
                with open(filename, 'w') as f:
                    f.write("\n".join(code_buffer))
                print(f"✓ Circuit saved to {filename}")
                speak(f"Saved to {filename}")
                continue

            # --- NEW: LOAD LOGIC ---
            if cmd_lower.startswith('load '):
                filename = line.split(' ', 1)[1].strip()
                if not filename.endswith('.tara'):
                    filename += '.tara'
                try:
                    with open(filename, 'r') as f:
                        code_buffer = [l.strip() for l in f.readlines() if l.strip()]
                    print(f"✓ Loaded {len(code_buffer)} commands from {filename}")
                    speak(f"Loaded {filename}")
                except FileNotFoundError:
                    print(f"Error: File {filename} not found.")
                    speak("File not found.")
                continue
            
            if cmd_lower == 'run':
                if not code_buffer:
                    print("Error: No commands to run.")
                    continue
                
                print("Processing instructions...")
                full_code = "\n".join(code_buffer)
                tokens = lexer.tokenize(full_code)
                
                qc = engine.compile(tokens)
                print("✓ Circuit generated successfully.")
                
                engine.save_diagram(qc, "tara_circuit.png")
                print("✓ Blueprint saved to tara_circuit.png")
                
                print("✓ Running simulation on Aer Simulator...")
                counts = engine.run_simulation(qc)
                
                print("\n" + "="*41)
                print_histogram(counts)
                print("="*41 + "\n")
                
                speak("Simulation complete.")
                code_buffer = [] # Reset buffer after run
            else:
                code_buffer.append(line)
                
        except Exception as e:
            print(f"\n[ERROR]: {e}")
            speak("I encountered an error.")

if __name__ == "__main__":
    main()