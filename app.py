import streamlit as st
from PIL import Image
import time
import plotly.express as px

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Rohan Yadav - Portfolio", page_icon="📊", layout="wide")

# ---------- CUSTOM CSS FOR STAR BACKGROUND ----------
custom_css = """
<style>
body {
    background: radial-gradient(circle at top left, #0d0d0d, #1c1c1c, #2e0854);
    background-size: cover;
    color: white;
    font-family: 'Segoe UI', sans-serif;
    overflow: hidden;
}

/* Stars Animation */
@keyframes move-stars {
    from {transform: translateY(0);}
    to {transform: translateY(-1000px);}
}

.stars {
    position: fixed;
    top: 0;
    left: 0;
    width: 200%;
    height: 200%;
    background: transparent url('https://www.transparenttextures.com/patterns/stardust.png') repeat;
    animation: move-stars 100s linear infinite;
    z-index: -1;
    opacity: 0.4;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: rgba(0,0,0,0.9);
    color: white;
}

/* Project Cards */
.project-card {
    background: rgba(255, 255, 255, 0.08);
    padding: 15px;
    border-radius: 10px;
    box-shadow: 2px 2px 10px rgba(255,255,255,0.1);
    transition: transform 0.2s;
    backdrop-filter: blur(8px);
}
.project-card:hover {
    transform: scale(1.03);
    box-shadow: 4px 4px 15px rgba(255,255,255,0.3);
}

h1, h2, h3, h4 {
    color: #E6E6FA;
}
a {
    color: #E6E6FA;
}
</style>
<div class="stars"></div>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ---------- SIDEBAR NAVIGATION ----------
tabs = ["Home", "About", "Projects", "Skills", "Contact"]
page = st.sidebar.radio("Navigation", tabs)

# ---------- HOME ----------
if page == "Home":
    st.title("Hi, I'm Rohan Yadav 👋")

    # Typing animation effect
    text = "Data Analyst | Python | SQL | Machine Learning"
    animated_text = ""
    for char in text:
        animated_text += char
        st.markdown(f"### {animated_text}")
        time.sleep(0.05)

    st.write("Welcome to my **portfolio website** built with Streamlit.")
    
    # Profile Image
    try:
        img = Image.open("profile.jpg")
        st.image(img, width=250)
    except:
        st.warning("Upload your profile.jpg in the app folder.")

    # Resume Download
    try:
        with open("resume.pdf", "rb") as file:
            st.download_button("📄 Download Resume", file, file_name="Rohan_Yadav_Resume.pdf")
    except:
        st.warning("Upload your resume.pdf in the app folder.")

# ---------- ABOUT ----------
elif page == "About":
    st.header("About Me")
    st.write("""
    I'm a **Data Analyst Intern** passionate about turning raw data into actionable insights.
    
    **Skills:**
    - Python (Pandas, NumPy, Matplotlib, Seaborn)
    - SQL
    - Excel
    - Machine Learning (Linear Regression, Random Forest)
    """)

# ---------- PROJECTS ----------
elif page == "Projects":
    st.header("My Projects")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='project-card'>
        <h3>📊 Supermart Grocery Sales Analysis</h3>
        <p>- Performed EDA & built Linear Regression model.<br>
        - Tools: Python, Pandas, Matplotlib, Scikit-learn</p>
        <a href="https://github.com/yourgithubusername/supermart-sales-analysis" target="_blank">View on GitHub</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='project-card'>
        <h3>🎬 Netflix Data Analysis</h3>
        <p>- Analyzed Netflix dataset for trends.<br>
        - Tools: Python, Pandas, Seaborn</p>
        <a href="https://github.com/yourgithubusername/netflix-analysis" target="_blank">View on GitHub</a>
        </div>
        """, unsafe_allow_html=True)

# ---------- SKILLS ----------
elif page == "Skills":
    st.header("Skills Overview")
    st.write("### Technical Skills")

    # Progress bars
    skill_chart = {
        "Python": 90,
        "SQL": 80,
        "Excel": 75,
        "Machine Learning": 70,
        "Data Visualization": 85
    }
    for skill, level in skill_chart.items():
        st.write(f"**{skill}**")
        st.progress(level)

    # Interactive chart with Plotly
    st.subheader("Skills Distribution")
    skills = list(skill_chart.keys())
    levels = list(skill_chart.values())
    fig = px.bar(x=skills, y=levels, color=skills, title="Skill Levels (%)", height=400)
    st.plotly_chart(fig)

# ---------- CONTACT ----------
elif page == "Contact":
    st.header("Contact Me")
    st.write("""
    📧 **Email:** rohan913069@gmail.com  
    🔗 **LinkedIn:** [Click Here](https://linkedin.com/in/yourprofile)  
    💻 **GitHub:** [Click Here](https://github.com/yourgithubusername)
    """)

    st.subheader("Send me a message:")
    with st.form(key="contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit = st.form_submit_button("Send")
        if submit:
            st.success(f"✅ Thanks {name}, your message has been sent!")
