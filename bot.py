
import os
import google.generativeai as genai

# This links your Key to my Brain
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_sy_gold_vibe():
    prompt = "Generate a fire 4-line afro-fusion song lyric for Sy Gold Ayomide about hustle and coding. Use Pidgin English."
    response = model.generate_content(prompt)
    print("🎵 NEW LYRIC GENERATED:")
    print(response.text)

if __name__ == "__main__":
    generate_sy_gold_vibe()
