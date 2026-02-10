import sys
import os

# 1. Ensure Python finds the SDK
sys.path.append(os.getcwd())

# 2. Import the actual classes from your files
from tara_sdk.core.lexer import Lexer
from tara_sdk.analysis.inspector import Inspector
from tara_sdk.backend.engine import QiskitEngine
from tara_sdk.utils.logger import setup_logger

# Setup CLI Logger
log = setup_logger("CLI")

def main():
    print("==========================================")
    print("   T.A.R.A. Quantum Compiler (v1.0)       ")
    print("==========================================")
    print("Type your commands. Type 'RUN' to execute the block.")
    
    # Initialize the Trinity (The 3 parts of the brain)
    lexer = Lexer()
    inspector = Inspector()
    engine = QiskitEngine()
    
    # Buffer to hold multiple lines of code
    code_buffer = []

    while True:
        try:
            # Get input
            line = input("   > ").strip()
        except KeyboardInterrupt:
            break
            
        # Exit Condition
        if line.lower() in ["exit", "quit"]:
            break
            
        # Run Condition
        if line.lower() == "run":
            if not code_buffer:
                print("⚠️  Buffer is empty. Add commands first.")
                continue

            # Combine lines into one script
            full_script = "\n".join(code_buffer)
            log.info("Compiling script...")
            
            # --- STEP 1: LEXER (Text -> Tokens) ---
            tokens = lexer.tokenize(full_script)
            
            if not tokens:
                print("❌ No valid tokens found.")
                code_buffer = []
                continue

            # --- STEP 2: INSPECTOR (Safety Check) ---
            is_safe, errors = inspector.analyze(tokens)
            
            if not is_safe:
                for err in errors:
                    print(f"❌ {err}")
                log.error("Safety checks failed. Aborting.")
                code_buffer = [] # Reset
                continue

            # --- STEP 3: ENGINE (Build Circuit) ---
            try:
                qc = engine.compile(tokens)
                print("\n" + str(qc))
                
                # Save the image
                output_file = "tara_circuit.png"
                engine.save_diagram(qc, output_file)
                print(f"\n✅ SUCCESS: Circuit saved to '{output_file}'")
            except Exception as e:
                print(f"❌ COMPILER ERROR: {e}")
            
            # Clear buffer for the next program
            code_buffer = []
        
        else:
            # Add line to buffer
            if line:
                code_buffer.append(line)

if __name__ == "__main__":
    main()