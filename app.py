import streamlit as st

# User ke interest ke basis par career suggest karne wali data
career_data = {
    "data science": {
        "career": "Data Scientist",
        "skills": "Python, Pandas, NumPy, Machine Learning, SQL",
        "path": "Python se start karo → Pandas/NumPy seekho → Machine Learning → Projects banao"
    },
    "machine learning": {
        "career": "ML Engineer",
        "skills": "Python, Scikit-learn, TensorFlow, Data Preprocessing",
        "path": "Python seekho → Algorithms samjho → Deep Learning → Models deploy karo"
    },
    "prompt writing": {
        "career": "Prompt Engineer",
        "skills": "English, Creativity, ChatGPT, Gemini, Prompt Tuning",
        "path": "AI model samjho → Prompt likhna seekho → Practice karo ChatGPT pe"
    },
    "ai ethics": {
        "career": "AI Ethics Expert",
        "skills": "Policy knowledge, Responsible AI, Bias control",
        "path": "AI basics seekho → AI ethics samjho → Real-world examples dekho"
    }
}

st.set_page_config(page_title="AI Career Advisor Bot")
st.title("🤖 AI Career Advisor Bot")
st.markdown("AI field mein career choose karne ke liye bot ka use karein.")

user_input = st.text_input("Apna interest likhein (e.g., data science, machine learning):").lower()

if user_input:
    if user_input in career_data:
        info = career_data[user_input]
        st.success(f"🎯 Career: {info['career']}")
        st.info(f"🧠 Skills: {info['skills']}")
        st.markdown(f"📚 Seekhne ka tareeqa: {info['path']}")
    else:
        st.warning("Try: data science, machine learning, prompt writing, ai ethics")
