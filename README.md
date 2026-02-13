 # T.A.R.A. (Text Automated Response Architecture) 🌌

**A Natural Language Quantum Compiler built in Python.**

T.A.R.A. allows users to design Quantum Circuits using plain English commands. It parses natural language, validates quantum logic via a Safety Inspector, simulates results, and renders professional circuit diagrams using Qiskit.

---

## Features
* **Natural Language Parsing:** Type "Spawn 2 qubits" or "Spin qubit 0" instead of writing boilerplate code.
* **Universal Gate Set:** Supports Hadamard (Spin), CNOT (Link), Phase (S), and T-gates for universal quantum computation.
* **Visualizer 2.0:** High-fidelity ASCII histograms rendered directly in your terminal for instant probability analysis.
* **Library Persistence:** Save and load quantum scripts using the custom `.tara` file format.
* **Universal Voice Feedback:** Cross-platform narration for macOS, Windows, and Linux.
* **Auto-Visualization:** Automatically generates high-definition circuit blueprints (`tara_circuit.png`).



---

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

3. Manage your library 

tara> save my_circuit
tara> clear
tara> load my_circuit

## Available CLI commands
run: Compiles the current buffer, generates the diagram, and runs the simulation.

clear: Wipes the current circuit buffer so you can start fresh.

exit: Shuts down the compiler and saves your session logs.

save [name]	Saves the current command buffer to a .tara file.

load [name]	Loads a saved .tara script into the buffer.

## T.A.R.A. comes pre-loaded with fundamental quantum algorithms. You can find them in the /library folder:

load library/teleport — Execute Quantum Teleportation across 3 qubits.

load library/superdense — Demonstrate 2-bit data transfer via 1-qubit.

load library/bell_test — Create maximum entanglement between two particles.

##  Project Architecture
```text
TaraQuantum/
├── library/             # Pre-built .tara algorithms
├── tara_sdk/            # Core Engine
│   ├── backend/         # Qiskit & Aer logic
│   ├── core/            # Lexer & Inspector
│   └── utils/           # Voice, Files, Visualizer
├── tara_cli.py          # Universal Entry Point
└── DEVLOG.md            # Version History