import streamlit as st

st.title("📚 StudyGenie AI")

# Input
subjects = st.text_input("Enter subjects (comma separated)")
hours = st.number_input("Study hours per day", 1, 12)

# Timetable
if st.button("Generate Plan"):
    subject_list = subjects.split(",")
    per_hour = hours / len(subject_list)

    st.subheader("📅 Study Plan")
    for sub in subject_list:
        st.write(f"{sub.strip()} → {round(per_hour,1)} hrs")

# Progress Tracker
st.subheader("✅ Progress")
for sub in subjects.split(","):
    if sub:
        st.checkbox(f"Completed {sub.strip()}")

# Doubt Solver
st.subheader("❓ Ask Doubt")
question = st.text_input("Enter your question")

if st.button("Get Answer"):
    st.write("💡 Answer:")
    st.write("This is a sample AI answer.")

# UI
st.info("Stay consistent 💪")
st.progress(60)
