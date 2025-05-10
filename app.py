import os
import streamlit as st
import geocoder
from textblob import TextBlob
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
groq_api_key = os.getenv("groq_api_key")
client = Groq(api_key=groq_api_key)

# Time check
current_hour = datetime.now().hour
is_night = current_hour >= 19 or current_hour <= 5

# Get user location
def get_location():
    g = geocoder.ip('me')
    return g.city if g.ok else "Delhi"

# Mood detection
def detect_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.5:
        return "excited"
    elif polarity > 0.1:
        return "happy"
    elif polarity < -0.5:
        return "angry"
    elif polarity < -0.1:
        return "sad"
    elif abs(polarity) < 0.1:
        return "bored"
    else:
        return "neutral"

# System prompt builder
def build_prompt(data, city):
    safety_note = ""
    if is_night and data["alone"] == "alone":
        safety_note = "Note: It's night, so suggest safe or indoor places like cafes, lounges, or relaxing home activities."

    return (
        f"The user is currently feeling '{data['mood']}' and is located in {city}.\n"
        f"They want to go out for a: {data['reason']}.\n"
        f"They plan to go {data['alone']}.\n"
        f"They want to spend time for a {data['duration']}\n"
        f"They enjoy activities related to: {data['preferences']}.\n"
        f"Their budget is: {data['budget']}.\n"
        f"Activity type preferred: {data['indoor_outdoor']}.\n"
        f"Restrictions to consider: {data['restrictions']}.\n"
        f"{safety_note}\n"
        f"Suggest 4-5 creative, uplifting, and safe places or things to do accordingly.\n"
        f"Include emojis and explain briefly why each option fits their emotional state and context and highlight the places."
    )

# Init session
if "conversation_stage" not in st.session_state:
    st.session_state.conversation_stage = 0
    st.session_state.user_data = {}
    st.session_state.history = []

st.title("🌟 Personalized Mood-Based Travel Guide")

model = st.sidebar.selectbox('Model', ['Mixtral-8x7b-32768', 'Llama3-70b-8192', 'Gemma-7b-It'])

# Main questions
questions = [
    "How are you exactly feeling right now?",
    "on what occasion are you going out? (e.g., birthday, date, etc.)",
    "Are you planning to go alone or with someone? (Type: alone / with someone)",
    "Do you want to go out for long or just a few hours? (Type: long / short)",
    "What kind of activities do you usually enjoy? (e.g., adventure, food, calm nature)",
    "What's your budget range for today? (Type: low / medium / high)",
    "Would you like indoor or outdoor activities? (Type: indoor / outdoor)",
    "Do you have any restrictions? (e.g., vegetarian, no long walks, etc.)"
]

keys = [
    "mood", "reason", "alone", "duration",
    "preferences", "budget",
    "indoor_outdoor", "restrictions"
]

if st.session_state.conversation_stage < len(questions):
    current_question = questions[st.session_state.conversation_stage]
    user_input = st.text_input(f"🗨️ {current_question}", key=f"input_{st.session_state.conversation_stage}")

    if st.button("Next"):
        if user_input.strip() == "":
            st.warning("Please enter a response before proceeding.")
        else:
            key = keys[st.session_state.conversation_stage]
            if key == "mood":
                st.session_state.user_data[key] = detect_mood(user_input)
            else:
                st.session_state.user_data[key] = user_input.lower()
            st.session_state.conversation_stage += 1
            st.rerun()
else:
    city = get_location()
    prompt = build_prompt(st.session_state.user_data, city)

    if st.button("Generate Recommendations"):
        chat_completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful travel assistant that suggests safe and creative places based on user mood, time, and preferences."},
                {"role": "user", "content": prompt}
            ]
        )

        response = chat_completion.choices[0].message.content
        st.session_state.history.append((prompt, response))

        st.success("✨ Here are your personalized recommendations:")
        st.markdown(response)