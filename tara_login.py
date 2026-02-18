import os
from qiskit_ibm_runtime import QiskitRuntimeService

def login():
    print("\n" + "="*40)
    print("      T.A.R.A. SECURE CLOUD LOGIN")
    print("="*40)
    
    # Use the ApiKey-23c2a55a... from your screenshot
    token = input("\n🔑 Enter IBM Cloud API Key: ").strip()
    
    # Use 'NamasteQuantum' (The name from your screenshot)
    instance = input("🏢 Enter Instance Name: ").strip()

    if not token or not instance:
        print("\n❌ Error: Key and Instance cannot be empty.")
        return

    print(f"⏳ Verifying '{instance}' on IBM Cloud...")
    try:
        # Save using the ibm_cloud channel
        QiskitRuntimeService.save_account(
            channel="ibm_cloud",
            token=token,
            instance=instance,
            overwrite=True
        )
        
        # Test connection
        QiskitRuntimeService(channel="ibm_cloud")
        print("\n✅ Success! NamasteQuantum is linked and verified.")
        
    except Exception as e:
        print(f"\n❌ Login failed. Error: {e}")
        try:
            QiskitRuntimeService.delete_account(channel="ibm_cloud")
        except:
            pass

if __name__ == "__main__":
    login()