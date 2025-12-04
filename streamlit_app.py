import streamlit as st

st.set_page_config(page_title="Daily Routine Improvement", page_icon="🌞")

st.title("🌞 Daily Routine Improvement Program 🌸")

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

sleep = st.number_input("How many hours do you sleep per day? 💤", min_value=0.0, max_value=24.0, step=0.5)
study = st.number_input("How many hours do you study or work per day? 📚", min_value=0.0, max_value=24.0, step=0.5)
fun = st.number_input("How many hours do you spend on fun or relaxation? 🎮", min_value=0.0, max_value=24.0, step=0.5)

if st.button("Analyze My Day 🧠"):
    total = sleep + study + fun
    
    st.write(f"### ⏱ Total accounted hours: {total} hours")
    
    if total > 24:
        st.error("❌ Total hours exceed 24! Please check your inputs.")
    else:
        st.success("✔ Analysis completed successfully!")

        if sleep < 6:
            st.write("😴 **Your sleep is low! Try increasing it for better health.**")
        elif sleep > 10:
            st.write("💤 **You sleep too much! Balance your time.**")
        else:
            st.write("✨ **Your sleep duration is perfect.**")

        if study < 3:
            st.write("📚 **Study time is low. Try increasing your study hours.**")
        elif study > 8:
            st.write("🧠 **You study too long! Take breaks.**")
        else:
            st.write("👌 **Study time is good.**")

        if fun < 1:
            st.write("🎮 **You have very little fun time! Give yourself a break.**")
        elif fun > 6:
            st.write("🤪 **Too much fun time! Try balancing more.**")
        else:
            st.write("🌸 **Fun time is well balanced.**")

st.write("---")
st.write("🔧 **This application was developed using Python and Streamlit.**")
