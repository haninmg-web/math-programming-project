import streamlit as st

st.set_page_config(page_title="Daily Routine Improvement", page_icon="🌞")

st.title("🌞 Daily Routine Improvement Program 🌸")

st.write("""
### 🎓 Project Information  
Course: Mathematical Programming  
Students:  
- Haneen Mosleh  
- Amal Saeed  
- Bayan Eid  
- Jana Abdullah  
- Jana Saleh  

**This project is created for the Mathematical Programming course.**

Supervised by: Dr. Reem Algethamie  
""")

sleep = st.number_input("How many hours do you sleep per day? 💤", min_value=0.0, max_value=24.0, step=0.5)
study = st.number_input("How many hours do you study or work per day? 📚", min_value=0.0, max_value=24.0, step=0.5)
fun = st.number_input("How many hours do you spend on fun or relaxation? 🎮", min_value=0.0, max_value=24.0, step=0.5)

if st.button("Analyze My Day"):
    total = sleep + study + fun

    st.write(f"🕒 **Total hours in your day: {total} hours**")

    if total > 24:
        st.error("⚠ Your total exceeds 24 hours! Please adjust your schedule.")
        st.stop()

    st.subheader("📊 Daily Routine Analysis:")

    if sleep < 6:
        st.write("- 😴 You’re not sleeping enough, try to rest more.")
    elif 6 <= sleep <= 8:
        st.write("- 👌 Your sleep time is perfect and balanced.")
    else:
        st.write("- 🌤 You’re sleeping too much, try to balance your day better.")

    if study < 3:
        st.write("- 📘 You’re studying/working too little, try to add more focus time.")
    elif 3 <= study <= 6:
        st.write("- 👏 Good amount of study/work time!")
    else:
        st.write("- 🌿 You’re spending too much time studying/working, take a break sometimes.")

    if fun < 1:
        st.write("- ❤️ You don’t have enough fun time, take a little break for yourself.")
    elif 1 <= fun <= 3:
        st.write("- 🎯 Balanced fun time!")
    else:
        st.write("- 💪 Too much fun time! Try to cut down a bit for productivity.")

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
