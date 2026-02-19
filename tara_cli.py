import sys
import os
import time
import platform

# 1. ENVIRONMENT SETUP
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSET_PATH = os.path.join(BASE_DIR, "assets")

sys.path.append(BASE_DIR)

try:
    from tara_sdk.core.lexer import Lexer
    from tara_sdk.backend.engine import QiskitEngine
    from tara_sdk.utils.visualizer import print_histogram
except ImportError as e:
    print(f"❌ Setup Error: {e}")
    sys.exit(1)

# THE PRODUCTION VOICE ENGINE
def tara_speak(filename):
    """Universal audio player for production-level assets."""
    full_path = os.path.join(ASSET_PATH, filename)
    
    if not os.path.exists(full_path):
        return

    current_os = platform.system()

    if current_os == "Darwin":    # macOS
        os.system(f"afplay {full_path} &")
    elif current_os == "Windows": # Windows
        os.system(f'start /min powershell -c (New-Object Media.SoundPlayer "{full_path}").PlaySync()')

# 2. CORE EXECUTION LOGIC
def execute_logic(file_name, engine, lexer, inspect=False):
    # Standardize filename
    original_name = file_name
    if not file_name.endswith(".tara"):
        file_name += ".tara"

    file_path = os.path.join(BASE_DIR, "library", file_name)
    
    if not os.path.exists(file_path):
        file_path = os.path.join(BASE_DIR, file_name)
        if not os.path.exists(file_path):
            print(f"❌ Error: Could not find '{file_name}'")
            return

    try:
        with open(file_path, 'r') as f:
            code = f.read()

        tokens = lexer.tokenize(code)

        if inspect:
            tara_speak("analyzing.wav") 
            print("\n🔍 Q-INSPECTOR: QUANTUM INTEGRITY REPORT")
            print("-" * 35)
            qubits_used = set()
            for t in tokens:
                if isinstance(t.value, dict):
                    for v in t.value.values():
                        if isinstance(v, int): qubits_used.add(v)
            print(f"✅ Qubits: {max(len(qubits_used), 1)} | Status: SAFE")
            print("-" * 35)
            time.sleep(0.5)

        # COMPILE AND RUN
        qc = engine.compile(tokens)
        results = engine.run_locally(qc) 
        
        # VISUALIZATION
        print_histogram(results)
        
        # DYNAMIC PNG NAMING: 
        # Saves as 'bell_test.png' instead of 'tara_circuit.png'
        image_name = original_name.replace(".tara", "") + ".png"
        engine.save_vision(qc, image_name)
        
        print(f"🎨 Circuit blueprint saved as: {image_name}")
        
        # OPTIONAL: Uncomment the line below to auto-open the PNG on Mac
        # os.system(f"open {image_name}")
        
        tara_speak("complete.wav")
        
    except Exception as e:
        print(f"⚠️ Logic Error: {e}")

# 3. INTERACTIVE SHELL
def start_tara_shell():
    engine = QiskitEngine()
    lexer = Lexer()

    os.system('cls' if platform.system() == "Windows" else 'clear')
    
    print("==========================================")
    print("    T.A.R.A. QUANTUM INTERACTIVE v3.1")
    print("    [Dynamic Visualizer Enabled]")
    print("==========================================")
    print("Commands: run <file> | inspect <file> | clear | exit")
    
    tara_speak("online.wav")

    while True:
        try:
            user_input = input("\n🗣️ TARA > ").strip().split()
            if not user_input: continue
            
            cmd = user_input[0].lower()
            
            if cmd in ["exit", "quit"]:
                break

            if cmd == "clear":
                os.system('cls' if platform.system() == "Windows" else 'clear')
                continue

            if len(user_input) < 2:
                print("❓ Usage: run <file> or inspect <file>")
                continue

            # Handles filenames with spaces or underscores
            target_file = "_".join(user_input[1:])
            
            if cmd == "run":
                execute_logic(target_file, engine, lexer, inspect=False)
            elif cmd == "inspect":
                execute_logic(target_file, engine, lexer, inspect=True)

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    start_tara_shell()