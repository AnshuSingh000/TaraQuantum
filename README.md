# T.A.R.A. (Text Automated Response Architecture)

**A Natural Language Quantum Compiler built in Python.**

T.A.R.A. allows users to design Quantum Circuits using plain English commands. It parses natural language, validates quantum logic via a Safety Inspector, and renders professional circuit diagrams using Qiskit.

## 🚀 Features
- **Natural Language Parsing:** "Create 3 qubits" instead of `qc = QuantumCircuit(3)`.
- **Safety Inspector:** Prevents runtime errors (e.g., entangling a qubit with itself) before execution.
- **Auto-Visualization:** Automatically generates and saves circuit diagrams (`.png`).
- **Voice Feedback:** T.A.R.A. speaks to confirm actions and warn about errors.
- **Expanded Gate Set:** Supports H (Hadamard), CX (CNOT), X (NOT), and Z (Phase) gates.

## 🛠️ Installation

```bash
# 1. Clone the repository
git clone [https://github.com/AnshuSingh000/TaraQuantum.git](https://github.com/AnshuSingh000/TaraQuantum.git)
cd TaraQuantum

# 2. Install core dependencies
pip install -r requirements.txt

# 3. Install Voice Module
pip install pyttsx3

# How to run TaraCompiler

Start the Program: Run the CLI from your terminal:

python tara_cli.py

Design Your Circuit: When you see the prompt (>), type commands like this:

create 3 qubits
h qubit 0
cx 0 with 1
x qubit 2
measure all
run


