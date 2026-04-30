import streamlit as st
import os

st.set_page_config(page_title="Skills | Honelyn Recto", page_icon="⚡", layout="wide")

# --- PATH LOGIC ---
# Get the current directory (the 'pages' folder)
base_path = os.path.dirname(__file__)

st.markdown("""
<h1 style='font-family:Syne,sans-serif;font-weight:800;font-size:48px;margin-bottom:8px;'>Skills</h1>
<div style='width:60px;height:4px;background:linear-gradient(90deg,#7c6af7,#e85d8a);border-radius:2px;margin-bottom:12px;'></div>
<p style='color:#7a7a96;font-size:16px;margin-bottom:32px;'>A snapshot of my technical toolkit and proficiency levels.</p>

<style>
    .card {
        padding: 10px;
        border-radius: 15px;
        background-color: #ffffff;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Category filter
category = st.selectbox("Filter by category:", ["All", "Frontend", "Backend", "Data & ML", "DevOps & Tools"])

all_skills = {
    "Frontend": [
        ("JavaScript ", 75), ("HTML & CSS", 90),
    ],
    "Backend": [
        ("Python", 80), 
    ],
    "Data & ML": [
        ("Pandas / NumPy", 50), ("Streamlit", 85),
        ("Matplotlib / Plotly", 50), ("SQL", 50),
    ],
    "DevOps & Tools": [
        ("Git / GitHub", 92), ("AI", 100),("Streamlit",90)
    ],
}

if category == "All":
    display_skills = {k: v for k, v in all_skills.items()}
else:
    display_skills = {category: all_skills[category]}

# Display Skill Bars
for cat, skills in display_skills.items():
    st.write(f"### {cat}")
    for skill_name, level in skills:
        st.text(skill_name)
        st.progress(level)

st.divider()
st.subheader("📜 Certificates")

# 1. Defined Data with exact filenames from your GitHub
# Note: Ensure these match the spelling and capitalization in your 'pages' folder exactly!
skills_data = [
    {"name": "Android App Development", "img": "Andriod_App_development_for_beginner.png"},
    {"name": "Introduction to IoT", "img": "Intoduction_to_IoT.png"},
    {"name": "Python Essentials", "img": "Python_Essential_1.png"},
    {"name": "Python for Beginners", "img": "Python_for_Beginner.png"},
    {"name": "Operating System Design", "img": "Operating_System_Design.png"},
    {"name": "Software Testing", "img": "Software_testing_and_quality_assurance.png"},
]

# 2. Grid Logic to prevent repetition or empty white boxes
cols_per_row = 3
for i in range(0, len(skills_data), cols_per_row):
    cols = st.columns(cols_per_row)
    chunk = skills_data[i : i + cols_per_row]
    
    for idx, skill in enumerate(chunk):
        # Construct path for images now located inside 'pages'
        img_path = os.path.join(base_path, skill["img"])
        
        with cols[idx]:
            if os.path.exists(img_path): # Only draw if image is found
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.image(img_path, use_container_width=True)
                st.caption(f"{skill['name']}")
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error(f"Image not found: {skill['img']}")