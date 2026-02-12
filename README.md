# T.A.R.A. (Text Automated Response Architecture)

**A Natural Language Quantum Compiler built in Python.**

TARA allows users to design Quantum Circuits using plain English commands. It parses natural language, validates quantum logic (Safety Inspector), and renders professional circuit diagrams using Qiskit.

## Features
- **Natural Language Parsing:** "Create 3 qubits" instead of `qc = QuantumCircuit(3)`.
- **Safety Inspector:** Prevents runtime errors (e.g., entangling a qubit with itself) before execution.
- **Auto-Visualization:** Automatically generates and saves circuit diagrams (`.png`).
- **Microservices Architecture:** Modular design (Lexer -> Inspector -> Engine).
- **Voice Feedback:** T.A.R.A. speaks to confirm actions and warn about errors.

## 🛠️ Installation

```bash
git clone [https://github.com/AnshuSingh000/TaraQuantum.git](https://github.com/AnshuSingh000/TaraQuantum.git)
cd TaraQuantum
python tara_cli.py
pip install pyttsx3
## ⚡ How to Run T.A.R.A.

1. **Start the Program:**
   Run the CLI from your terminal:
   ```bash
   python tara_cli.py
    
2. Design Your Circuit When you see the prompt ( >), type these commands one by one:

create 3 qubits
h qubit 0
cx 0 with 1
measure all
run

3.See the Result Check your folder for a new image called tara_circuit.png. It will look like this: