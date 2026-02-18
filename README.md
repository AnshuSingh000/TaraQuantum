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



# T.A.R.A. v2.0 - Tactical Asynchronous Quantum Assistant

T.A.R.A. is a specialized CLI-driven Quantum SDK designed for low-latency circuit compilation and execution on IBM's 2026 Heron-class hardware.

## 🚀 Current Status: Phase 1 Complete
- **Backend:** IBM Quantum Runtime (V2 Primitives)
- **Target Hardware:** `ibm_torino` (via NamasteQuantum Instance)
- **Architecture:** Asynchronous Job Tracking with Persistent Memory

## 🛠 Features
- **Smart Cloud Manager:** Automatically handles ISA (Instruction Set Architecture) transpilation.
- **Job Memory:** Persistent `job_history.txt` so you never have to manually track 20-character Job IDs.
- **Voice Feedback:** Cross-platform OS text-to-speech for job status updates.

## ⌨️ Command Set
| Command | Action |
| :--- | :--- |
| `add put [gate] on [q]` | Add a gate to the local buffer. |
| `run` | Execute circuit on local simulator. |
| `run --cloud` | Submit circuit to NamasteQuantum practice hub. |
| `check [ID/last]` | Retrieve results from IBM Quantum. |
| `history` | List all previous Job IDs. |
| `clear` | Wipe the current circuit buffer. |

# T.A.R.A. v2.5 - The Autonomy Update

**"Removing the barriers between the developer and the quantum field."**

## The Strategic Pivot: Cloud-Independent Execution
Following the successful hardware benchmarks on `ibm_torino` in v2.0, the project encountered significant infrastructure friction with centralized cloud providers. Persistent authentication latency and regional service outages in the Washington DC (us-east) data center led to a critical design realization: **A compiler is only as powerful as its accessibility.**

To ensure 100% reliability and uphold the "Social Good" mission of the project, T.A.R.A. has been redirected to a **Local-First Architecture**.

## 🛠️ Key Redirection Features
* **Zero-Friction Access:** Removed mandatory IBM Cloud login requirements. Users can now compile and run logic instantly without third-party authentication.
* **Local Engine Primacy:** Integrated high-performance local simulation as the default backend. This eliminates the "Cloud Gatekeeper" problem and provides zero-cost execution.
* **Hardware-Agnostic Logic:** The T.A.R.A. Lexer now focuses on universal quantum instructions, ensuring that code written today will be portable to any hardware provider in the future.
## 🛠️ Diagnostic & Recovery Suite (Legacy Support)

During the transition to v2.5, a suite of diagnostic tools was developed to attempt full cloud synchronization. While the system now defaults to local execution, these tools remain available for advanced verification:

* `fix_everything.py`: Automated mapping of API keys to specific Service Instances.
* `debug_login.py`: Deep-clean utility to purge corrupted local credentials.
* `tara_login.py`: Secure gateway for V2 Primitives (Sampler/Estimator) integration.

##  Professional Philosophy
This update represents a transition from a **Cloud-Dependent Tool** to a **Sovereign Quantum Platform**. By decoupling from unstable third-party infrastructures, T.A.R.A. empowers the user with complete control over their quantum development environment.



---