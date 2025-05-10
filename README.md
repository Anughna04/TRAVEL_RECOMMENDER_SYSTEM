## TRAVEL_RECOMMENDER_SYSTEM
### Your Mood. Your City. Your Vibe.

## 📌 Overview
TravelMate is a mood-aware travel recommendation app built with Streamlit and LLMs (Groq API models like LLaMA3 and Mixtral). It detects user mood using sentiment analysis, factors in location, time of day, personal preferences, and generates personalized travel or activity suggestions. Perfect for spontaneous plans, mood-lifters, or self-care trips!

## 🎥 Demo Video
![Demo GIF](SmartHireX_demo.gif)

## 📌 Features
- ✅ Sentiment-Aware Suggestions – Uses TextBlob to classify user mood and tailor activity recommendations.
- ✅ Time & Safety Aware – Considers whether it's night and gives safer indoor suggestions if alone.
- ✅ Location-Based Context – Auto-detects user city via IP for relevant local recommendations.
- ✅ LLM-Powered Planning – Uses Groq-hosted LLMs (LLaMA3, Mixtral, etc.) to generate creative, uplifting plans.
- ✅ Interactive Chat Flow – Conversational, step-by-step interface for collecting user preferences.
- ✅ Beautiful & Clean UI – Built with Streamlit for an elegant user experience.

## 🚀 Technologies Used
- Programming Language: Python 🐍
- Web Framework: Streamlit 🌐
- Sentiment Detection: TextBlob 💬
- Geolocation: geocoder 🌍
- LLM API: Groq (LLaMA3, Mixtral-8x7b, Gemma) 🤖
- Date/Time Awareness: datetime module
- Environment Variables: dotenv

## 🔧 Installation & Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Anughna04/TRAVEL_RECOMMENDER_SYSTEM.git
   cd TRAVEL_RECOMMENDER_SYSTEM
   ```

2. **Install Required Libraries:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set Up Environment Variables:**
   Create a .env file and add your Groq API key:
   ```
   groq_api_key=your_groq_api_key_here
   ```
4. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```

##  How It Works
- The user answers 8 short questions about mood, occasion, companions, duration, preferences, etc.
- Sentiment is extracted using TextBlob to classify moods like happy, sad, bored, excited, angry.
- The system builds a custom prompt using all input data.
- A Groq-hosted LLM (user can choose between LLaMA3, Mixtral, or Gemma) generates 4–5 relevant suggestions.
- Suggestions are enhanced with emojis and explanations tied to mood, time, and safety.

---
### 📧 Contact
For any queries, reach out to **[anughnakandimalla11@gmail.com](mailto:anughnakandimalla11@gmail.com)**.
