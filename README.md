# T.A.R.A. (Text Automated Response Architecture)

**A Natural Language Quantum Compiler built in Python.**

T.A.R.A. allows users to design Quantum Circuits using plain English commands. It parses natural language, validates quantum logic via a Safety Inspector, simulates the results, and renders professional circuit diagrams using Qiskit.

## Features
- **Natural Language Parsing:** Type "Create 3 qubits" instead of writing boilerplate code.
- **Simulation Engine:** Built-in `qiskit-aer` support to run circuits and get probability results.
- **High-Level Macros:** Use commands like `entangle 0 and 1` to generate complex gate patterns instantly.
- **Auto-Visualization:** Automatically generates and saves circuit diagrams (`tara_circuit.png`).
- **Voice Feedback:** Native macOS voice integration to confirm actions and report results.

## 🛠️ Installation

```bash
# 1. Clone the repository
git clone [https://github.com/AnshuSingh000/TaraQuantum.git](https://github.com/AnshuSingh000/TaraQuantum.git)
cd TaraQuantum

# 2. Install dependencies
pip install -r requirements.txt
pip install qiskit-aer

# How to run TaraCompiler

1. Start the Program: Run the CLI from your terminal:

python tara_cli.py

2. Design Your Circuit: When you see the prompt (>), type commands like this:

create 3 qubits
entangle 0 and 1
measure all
run


