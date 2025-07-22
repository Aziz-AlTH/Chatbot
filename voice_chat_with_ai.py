import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import os
import cohere
import pyttsx3

# --------- CONFIG ---------
COHERE_API_KEY = "AtrNMrDlJCZOK0tlh7J5oJXZJSvyPm8CwSuc5CO3"  # 🔑 استبدل هذا بمفتاحك من Cohere
DURATION = 5 # عدد ثواني تسجيل الصوت
FILENAME = "input.wav"
# --------------------------

def record_audio(filename=FILENAME, duration=DURATION, fs=44100):
    print("🎙️ تسجيل الصوت جاري لمدة", duration, "ثواني...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, audio)
    print("✅ تم حفظ التسجيل في", filename)

def speech_to_text(filename=FILENAME):
    if not os.path.exists(filename):
        print("❌ ملف الصوت غير موجود:", filename)
        return ""
    print("🔍 تحميل نموذج Whisper...")
    model = whisper.load_model("base")
    print("🧠 تحويل الصوت إلى نص...")
    result = model.transcribe(filename)
    return result["text"]

def get_response(prompt):
    if not prompt.strip():
        return "لم يتم سماع أي كلام."
    print("🤖 إرسال إلى Cohere...")
    co = cohere.Client(COHERE_API_KEY)
    response = co.generate(
        model='command-r-plus',
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
    )
    return response.generations[0].text.strip()

def speak_text(text):
    if not text.strip():
        print("⚠️ لا يوجد نص لتحويله إلى صوت.")
        return
    print("🔊 تشغيل الرد الصوتي...")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    print("🚀 البرنامج يعمل الآن...")

    record_audio()

    user_text = speech_to_text()
    print("📝 النص:", user_text)

    ai_reply = get_response(user_text)
    print("💬 الرد:", ai_reply)

    speak_text(ai_reply)

    print("✅ انتهى البرنامج.")

if __name__ == "__main__":
    main()
