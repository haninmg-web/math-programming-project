import streamlit as st

st.set_page_config(page_title="Daily Routine Improvement", page_icon="🌞")

st.title("🌞 Daily Routine Improvement Program 🌸")

# -------------------------------
# Project Information Section
# -------------------------------
st.markdown("""
### 👩‍💻 Project Authors:
- Haneen Mosleh  
- Amal Saeed  
- Bayan Eid  
- Jannah Abdullah  
- Jannah Saleh  

### 🧑‍🏫 Supervised by:
- Dr. Reem Algethamie  

### 📘 Mathematical Programming Course Project
""")
# -------------------------------
# User Inputs
# -------------------------------
sleep = st.number_input("How many hours do you sleep per day? 💤", min_value=0.0, max_value=24.0, step=0.5)
study = st.number_input("How many hours do you study or work per day? 📚", min_value=0.0, max_value=24.0, step=0.5)
fun = st.number_input("How many hours do you spend on fun or relaxation? 🎮", min_value=0.0, max_value=24.0, step=0.5)

# -------------------------------
# Analysis Button
# -------------------------------
if st.button("Analyze My Day ✨"):
    total = sleep + study + fun

    st.write(f"🕒 **Total hours in your day: {total} hours**")

    if total > 24:
        st.error("⚠ Your total hours exceed 24! Please adjust your schedule.")
        st.stop()

    st.subheader("📊 Daily Routine Analysis:")

    # Sleep analysis
    if sleep < 6:
        st.write("- 😴 You are not sleeping enough, try to rest more.")
    elif 6 <= sleep <= 8:
        st.write("- 👌 Your sleep time is perfect and balanced.")
    else:
        st.write("- 🌤 You’re sleeping too much, try to balance your day better.")

    # Study/work analysis
    if study < 3:
        st.write("- 📘 You are studying/working too little, try to add more focus time.")
    elif 3 <= study <= 6:
        st.write("- 👏 Good amount of study/work time!")
    else:
        st.write("- 🌿 You are spending too much time studying/working, take breaks sometimes.")

    # Fun/relaxation analysis
    if fun < 1:
        st.write("- ❤️ You don’t have enough fun time, take a little break for yourself.")
    elif 1 <= fun <= 3:
        st.write("- 🎯 Balanced fun time!")
    else:
        st.write("- 💪 Too much fun time! Try to cut down a bit for productivity.")

    # Balance score
    balanceScore = (
        (6 <= sleep <= 8) +
        (3 <= study <= 6) +
        (1 <= fun <= 3)
    ) / 3 * 100

    st.write(f"💫 **Your daily balance score: {balanceScore}%**")

    if balanceScore == 100:
        st.success("🔥 Perfect! Your day is completely balanced.")
    elif balanceScore >= 70:
        st.success("💖 Great job! Your day is well balanced.")
    elif balanceScore >= 50:
        st.warning("💭 Your day is somewhat balanced, but needs a few adjustments.")
    else:
        st.error("🕊 You might need to reorganize your day from scratch.")

    st.write("✨ Thanks for using the Daily Routine Improvement Program! ✨")
