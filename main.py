import requests
import random
import string
import time
import sys

# --- CONFIGURATION ---
# Yahan us website ka registration URL dalein jahan ID lagani hai
TARGET_URL = "https://example.com/api/register" 

def generate_fake_data():
    """Random Name aur Mobile Number banane ke liye"""
    name = ''.join(random.choices(string.ascii_lowercase, k=6)).capitalize()
    # Fake Indian Mobile Number (9 se start hone wala)
    mobile = "9" + "".join(random.choices(string.digits, k=9))
    return name, mobile

def run_task(ref_id, count=15):
    print(f"🚀 Starting {count} registrations for Ref: {ref_id}")
    
    for i in range(1, count + 1):
        name, mobile = generate_fake_data()
        
        # Form Data (Isse website ke hisab se badalna pad sakta hai)
        payload = {
            "username": name,
            "mobile": mobile,
            "referral_id": ref_id,
            "password": "User@123",
            "confirm_password": "User@123"
        }
        
        try:
            # Website par data bhejna
            response = requests.post(TARGET_URL, data=payload, timeout=10)
            
            if response.status_code == 200:
                print(f"✅ ID {i} Success: {name} ({mobile})")
            else:
                print(f"⚠️ ID {i} Failed: Status {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error at ID {i}: {e}")
            
        # 2 second ka gap taaki server ko doubt na ho
        time.sleep(2)

if __name__ == "__main__":
    # GitHub Action se input lene ke liye
    if len(sys.argv) > 1:
        user_ref = sys.argv[1]
        run_task(user_ref)
    else:
        print("Error: No Referral ID provided!")
