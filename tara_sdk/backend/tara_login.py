import os
from qiskit_ibm_runtime import QiskitRuntimeService

def login():
    print("\n--- T.A.R.A. Secure Login ---")
    token = input("Enter your IBM Quantum API Token: ").strip()
    instance = input("Enter your Instance (e.g., hub/group/project): ").strip()

    if not token or not instance:
        print("❌ Error: Token and Instance are required.")
        return

    try:
        # This saves the credentials to your Mac's disk (~/.qiskit/qiskit-ibm.json)
        QiskitRuntimeService.save_account(
            channel="ibm_quantum",
            token=token,
            instance=instance,
            overwrite=True
        )
        print("\n✅ Success! Credentials saved to your system.")
        print("T.A.R.A. is now linked to your IBM account.")
    except Exception as e:
        print(f"\n❌ Login failed: {e}")

if __name__ == "__main__":
    login()