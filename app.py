import streamlit as st

from tools import (
    analyze_skill_gap,
    generate_career_plan,
    evaluate_interview_answer
)

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 CareerPilot AI")
st.write("Your autonomous career preparation assistant")

st.divider()

target_role = st.selectbox(
    "🎯 Target Role",
    [
        "Software Developer",
        "Data Analyst",
        "AI Engineer"
    ]
)

skills_text = st.text_input(
    "💻 Your Skills",
    placeholder="Example: C, Python, SQL"
)

if st.button("🔎 Analyze My Career", type="primary"):

    skills = [
        skill.strip()
        for skill in skills_text.split(",")
        if skill.strip()
    ]

    if not skills:
        st.warning("Please enter at least one skill.")
    else:
        result = analyze_skill_gap(
            skills,
            target_role
        )

        st.subheader("🎯 Skill Gap")

        col1, col2 = st.columns(2)

        with col1:
            st.write("### ✅ Matched Skills")
            st.write(result["matched_skills"])

        with col2:
            st.write("### 📚 Missing Skills")
            st.write(result["missing_skills"])

        st.info(result["recommendation"])

        plan = generate_career_plan(
            target_role,
            result["missing_skills"],
            30
        )

        st.subheader("📅 30-Day Career Plan")

        for i, item in enumerate(plan["plan"], 1):
            st.write(f"**{i}.** {item}")


st.divider()

st.subheader("🎤 Interview Practice")

question = st.text_input(
    "Interview Question",
    placeholder="Tell me about yourself."
)

answer = st.text_area(
    "Your Answer",
    placeholder="Type your interview answer here..."
)

if st.button("📊 Evaluate Answer"):

    if not question or not answer:
        st.warning("Enter both the question and your answer.")
    else:
        evaluation = evaluate_interview_answer(
            question,
            answer,
            target_role
        )

        st.write("### Result")
        st.write("**Quality:**", evaluation["quality"])
        st.write("**Feedback:**", evaluation["feedback"])
        st.write("**Next Action:**", evaluation["next_action"])
