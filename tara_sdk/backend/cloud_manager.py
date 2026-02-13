import os
from dotenv import load_dotenv
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

load_dotenv()

class CloudManager:
    def __init__(self):
        self.token = os.getenv("IBMQ_TOKEN")
        try:
            # Connect to IBM Quantum. 
            # Note: instance="ibm-q/open/main" is the standard path. 
            # If your 'NamasteQuantum' has a custom path, update it here.
            self.service = QiskitRuntimeService(
                channel="ibm_quantum_platform", 
                token=self.token,
                instance="ibm-q/open/main" 
            )
            print("✨ T.A.R.A. v2.0: Cloud Handshake Successful.")
        except Exception:
            self.service = QiskitRuntimeService(channel="ibm_quantum_platform", token=self.token)
            print("✨ T.A.R.A. v2.0: Connected (Auto-Discovery).")

    def execute_on_hardware(self, circuit):
        if not self.service: return None

        try:
            backend = self.service.least_busy(simulator=False, operational=True)
            print(f"🛰️ Routing to Real Hardware: {backend.name}...")

            if not circuit.cregs:
                circuit.measure_all()

            # Transpilation is mandatory for V2 Primitives
            pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
            isa_circuit = pm.run(circuit)

            sampler = Sampler(mode=backend)
            job = sampler.run([isa_circuit])
            return job
            
        except Exception as e:
            print(f"❌ Cloud Execution Error: {e}")
            return None

    def get_job_results(self, job_id):
        """Fetch results from the cloud once the job is DONE."""
        try:
            job = self.service.job(job_id)
            # FIX: Check the status string directly (no .name attribute needed)
            status = str(job.status())
            
            if status == "JobStatus.DONE" or status == "DONE":
                result = job.result()
                # Accessing the first PUB (Primitive Unified Bloc) result
                # and grabbing the bitstring counts
                return result[0].data.meas.get_counts()
            
            return f"Status: {status}"
        except Exception as e:
            return f"Error retrieving job: {e}"