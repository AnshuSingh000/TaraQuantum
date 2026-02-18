from qiskit_ibm_runtime import QiskitRuntimeService

def deep_clean_login():
    # 1. Clear any old, broken saved accounts from your Mac's memory
    try:
        QiskitRuntimeService.delete_account(channel="ibm_cloud")
        QiskitRuntimeService.delete_account(channel="ibm_quantum_platform")
        print("🧹 Local config cleared.")
    except:
        pass

    # Your verified credentials from the screenshots
    token = "ApiKey-23c2a55a-a33f-491c-9bef-2d08e0719126"
    # This is the exact CRN string from your dashboard
    crn = "crn:v1:bluemix:public:quantum-computing:us-east:a/402f72bef02247fdbc47164d5d657ec6:fd9132db-b1b5-4d7a-bc06-0bad4c2ee543::"

    print(f"⏳ Attempting fresh link via CRN...")
    try:
        # We test the connection immediately
        service = QiskitRuntimeService(
            channel="ibm_cloud", 
            token=token, 
            instance=crn
        )
        
        # If it works, save it for T.A.R.A. to use later
        QiskitRuntimeService.save_account(
            channel="ibm_cloud",
            token=token,
            instance=crn,
            overwrite=True
        )
        print("✅ SUCCESS! T.A.R.A. is finally linked to IBM Cloud.")
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        print("\nPossible fix: Go to IBM Cloud 'Access (IAM)' and ensure your API Key has 'Manager' access to Quantum.")

if __name__ == "__main__":
    deep_clean_login()