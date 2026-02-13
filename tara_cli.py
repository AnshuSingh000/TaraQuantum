import os
import platform
from tara_sdk.core.lexer import Lexer
from tara_sdk.backend.engine import QiskitEngine
from tara_sdk.backend.cloud_manager import CloudManager
from tara_sdk.utils.visualizer import print_histogram

# Persistent history file to keep track of those long IDs
HISTORY_FILE = "job_history.txt"

def speak(text):
    current_os = platform.system()
    try:
        if current_os == "Darwin": os.system(f"say '{text}' &")
        elif current_os == "Windows":
            ps_cmd = f'Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak("{text}")'
            os.system(f'powershell -Command "{ps_cmd}" &')
    except Exception: pass

def save_job_id(job_id):
    with open(HISTORY_FILE, "a") as f:
        f.write(f"{job_id}\n")

def get_last_job_id():
    if not os.path.exists(HISTORY_FILE): return None
    with open(HISTORY_FILE, "r") as f:
        lines = f.readlines()
        return lines[-1].strip() if lines else None

def main():
    print("-" * 50)
    print("T.A.R.A. v2.0 - Cloud-Integrated Quantum Compiler")
    print("Commands: 'run', 'run --cloud', 'check', 'history', 'clear', 'exit'")
    print("-" * 50)
    
    lexer = Lexer()
    engine = QiskitEngine()
    cloud = CloudManager() 
    
    code_buffer = []
    
    while True:
        try:
            line = input("tara> ").strip()
            if not line: continue
            cmd_lower = line.lower()

            if cmd_lower == 'exit':
                speak("Shutting down.")
                break

            elif cmd_lower == 'clear':
                code_buffer = []
                print("✓ Buffer cleared.")
                continue

            # NEW: Smart Check (Auto-uses the last ID if you just type 'check')
            elif cmd_lower.startswith('check'):
                parts = line.split()
                # If you just type 'check', it looks for the last saved ID
                job_id = parts[1] if len(parts) > 1 else get_last_job_id()
                
                if not job_id:
                    print("❌ No Job ID found. Run a cloud job first!")
                    continue
                
                print(f"🔍 Accessing ibm_torino for job: {job_id}...")
                status_or_results = cloud.get_job_results(job_id)
                
                if isinstance(status_or_results, dict):
                    print(f"✅ Job {job_id} is DONE!")
                    print_histogram(status_or_results)
                    speak("Results are in.")
                else:
                    print(f"⏳ {status_or_results}") 
                continue

            # NEW: History Command
            elif cmd_lower == 'history':
                if os.path.exists(HISTORY_FILE):
                    print("\n--- 📜 Recent NamasteQuantum Jobs ---")
                    with open(HISTORY_FILE, "r") as f:
                        for i, j_id in enumerate(f.readlines(), 1):
                            print(f"{i}. {j_id.strip()}")
                else:
                    print("History is empty.")
                continue

            elif cmd_lower.startswith('run'):
                if not code_buffer:
                    print("Error: Circuit is empty.")
                    continue
                
                tokens = lexer.tokenize("\n".join(code_buffer))
                qc = engine.compile(tokens)
                
                if '--cloud' in cmd_lower:
                    speak("Sending to IBM.")
                    job = cloud.execute_on_hardware(qc)
                    if job:
                        new_id = job.job_id()
                        save_job_id(new_id) # Save to file immediately
                        print(f"🚀 Job is live! ID: {new_id}")
                        print(f"📌 Tip: Type 'check' to see results.")
                else:
                    print("✓ Running local simulation...")
                    counts = engine.run_simulation(qc)
                    print_histogram(counts)
                
                code_buffer = [] 
            
            elif cmd_lower.startswith(('save ', 'load ')):
                filename = line.split(' ', 1)[1].strip()
                if not filename.endswith('.tara'): filename += '.tara'
                if cmd_lower.startswith('save'):
                    with open(filename, 'w') as f: f.write("\n".join(code_buffer))
                    print(f"✓ Saved to {filename}")
                else:
                    with open(filename, 'r') as f: code_buffer = [l.strip() for l in f.readlines()]
                    print(f"✓ Loaded {len(code_buffer)} commands.")
            
            else:
                code_buffer.append(line)
                
        except Exception as e:
            print(f"\n[ERROR]: {e}")
            speak("Error encountered.")

if __name__ == "__main__":
    main()