# T.A.R.A. (Text Automated Response Architecture)

**A Natural Language Quantum Compiler built in Python.**

T.A.R.A. allows users to design Quantum Circuits using plain English commands. It parses natural language, validates quantum logic via a Safety Inspector, simulates results, and renders professional circuit diagrams using Qiskit.

## 🚀 Features
- **Natural Language Parsing:** Type "Create 3 qubits" or "Spin qubit 0" instead of writing boilerplate code.
- **Universal Voice Feedback:** Cross-platform support for macOS (`say`), Windows (`PowerShell`), and Linux (`espeak`).
- **Advanced Physics Engine:** Supports a Universal Gate Set including Hadamard, CNOT, and Phase gates (S and T).
- **Simulation & Interference:** Built-in `qiskit-aer` support to observe quantum interference patterns.
- **Auto-Visualization:** Automatically generates high-definition circuit diagrams (`tara_circuit.png`).
- **Visualizer 2.0:** Built-in ASCII histogram for instant probability analysis.

## 🛠️ Installation

```bash
# 1. Clone the repository
git clone [https://github.com/AnshuSingh000/TaraQuantum.git](https://github.com/AnshuSingh000/TaraQuantum.git)
cd TaraQuantum

# 2. Install core dependencies
pip install -r requirements.txt
pip install qiskit-aer

# How to run TaraCompiler

1. Start the Program: Run the CLI from your terminal:

python tara_cli.py

2. Design Your Circuit: When you see the prompt (>), type commands like this:

tara> add 2 qubits
tara> spin qubit 0
tara> link 0 with 1
tara> observe all
tara> run

# Available CLI commands
run: Compiles the current buffer, generates the diagram, and runs the simulation.

clear: Wipes the current circuit buffer so you can start fresh.

exit: Shuts down the compiler and saves your session logs.


