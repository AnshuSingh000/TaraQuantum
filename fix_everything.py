import os
from qiskit_ibm_runtime import QiskitRuntimeService

def final_quantum_connection():
    print("\n" + "="*50)
    print("       T.A.R.A. FINAL CONNECTION SYNC")
    print("="*50)
    
    # 1. Your verified API Key from the IAM Dashboard
    API_KEY = "ApiKey-23c2a55a-a33f-491c-9bef-2d08e0719126"
    
    # 2. The exact CRN for NamasteQuantum in Washington DC (us-east)
    # This was pulled directly from your Resource List screenshot
    INSTANCE_CRN = "crn:v1:bluemix:public:quantum-computing:us-east:a/402f72bef02247fdbc47164d5d657ec6:fd9132db-b1b5-4d7a-bc06-0bad4c2ee543::"

    print(f"⏳ Attempting connection to Washington DC data center...")
    
    try:
        # Force a fresh connection using the new Qiskit Runtime permissions
        service = QiskitRuntimeService(
            channel="ibm_cloud", 
            token=API_KEY, 
            instance=INSTANCE_CRN
        )
        
        # Save this account permanently to your MacBook
        QiskitRuntimeService.save_account(
            channel="ibm_cloud",
            token=API_KEY,
            instance=INSTANCE_CRN,
            overwrite=True
        )
        
        print("\n✅ SUCCESS! Connection established.")
        print(f"📍 Instance: NamasteQuantum (Active)")
        print(f"🚀 T.A.R.A. is now linked to IBM Cloud.")
        
        # List available backends just to be sure
        backends = service.backends()
        print(f"📡 Available simulators/hardware: {len(backends)} systems found.")
        
    except Exception as e:
        print("\n❌ CONNECTION FAILED")
        print(f"Error details: {str(e)}")
        print("\nTroubleshooting Tip: If you just added the 'Qiskit Runtime' role,")
        print("it can take up to 5-10 minutes for IBM's global security to update.")

if __name__ == "__main__":
    final_quantum_connection()