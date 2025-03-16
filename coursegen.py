import streamlit as st

# Set Page Configuration
st.set_page_config(page_title="LearnHub", layout="wide")

# App title and description
st.markdown("""
    <style>
    .main-title {font-size:48px; color:#4CAF50; text-align:center;}
    .subtitle {font-size:24px; color:#555; text-align:center; margin-bottom:30px;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">LearnHub: Interactive Learning App</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Empowering Learning with Interactive Modules</div>', unsafe_allow_html=True)

# Sidebar Navigation
menu = ["Home", "Courses", "Quiz", "Progress Tracker"]
choice = st.sidebar.selectbox("Navigate", menu)

# Course Data
courses = ["Python Basics", "Java Fundamentals", "Basics of AI/ML", "Cybersecurity Essentials", "Data Science"]
quiz_questions = {
    "Python Basics": ("What is the keyword to define a function in Python?", ["def", "function", "define"], "def"),
    "Java Fundamentals": ("Which keyword is used to inherit a class in Java?", ["extends", "inherits", "super"], "extends"),
    "Basics of AI/ML": ("Which type of learning involves labeled data?", ["Supervised", "Unsupervised", "Reinforcement"], "Supervised"),
    "Cybersecurity Essentials": ("What does 'VPN' stand for?", ["Virtual Private Network", "Virtual Public Network", "Variable Private Network"], "Virtual Private Network"),
    "Data Science": ("Which library is widely used for data manipulation in Python?", ["Pandas", "NumPy", "SciPy"], "Pandas")
}

# Home Page
if choice == "Home":
    st.markdown("""
        <div style='font-size:18px;'>
        Welcome to <strong>LearnHub</strong>! Dive into interactive courses, test your knowledge with quizzes, and monitor your progress along the way.
        </div>
    """, unsafe_allow_html=True)

# Courses Page
elif choice == "Courses":
    st.header("Available Courses")
    course = st.selectbox("Choose a Course", courses)
    st.write(f"### {course}")
    st.info("Content coming soon!")

# Quiz Page
elif choice == "Quiz":
    st.header("Test Your Knowledge")
    selected_course = st.selectbox("Select Course for Quiz", courses)
    question, options, correct_answer = quiz_questions[selected_course]
    answer = st.radio(question, options)
    if st.button("Submit Answer"):
        if answer == correct_answer:
            st.success("Correct!")
        else:
            st.error("Incorrect. Try again.")

# Progress Tracker
elif choice == "Progress Tracker":
    st.header("Your Progress")
    daily_progress = st.slider("Daily Progress %", 0, 100, 50)
    weekly_progress = st.slider("Weekly Progress %", 0, 100, 70)

    st.subheader("Daily Progress")
    st.progress(daily_progress / 100)
    if daily_progress >= 70:
        st.success("Great daily progress!")
    elif daily_progress >= 40:
        st.info("You're halfway through today's goals!")
    else:
        st.warning("Need to focus more today!")

    st.subheader("Weekly Progress")
    st.progress(weekly_progress / 100)
    if weekly_progress >= 70:
        st.success("Great weekly progress!")
    elif weekly_progress >= 40:
        st.info("You're halfway through this week's goals!")
    else:
        st.warning("Let's catch up this week!")

st.sidebar.markdown("---")
st.sidebar.info("For assistance, contact support@learnhub.com")

