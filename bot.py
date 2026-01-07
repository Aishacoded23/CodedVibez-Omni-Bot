import os

def start_vibe():
    print("🚀 CodedVibez Omni-Bot is Active!")
    print("Sy Gold Ayomide Vibes loading...")
    # This is where your Gemini Key will work
    key = os.getenv('GEMINI_API_KEY')
    if key:
        print("✅ Connection to Gemini AI Successful!")
    else:
        print("❌ Error: Gemini Key not found.")

if __name__ == "__main__":
    start_vibe()
