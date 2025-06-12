from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | K Krishna Chaithanya"
PAGE_ICON = "📋"
NAME = "K Krishna Chaithanya"
DESCRIPTION = """
An aspiring Python Developer with hands-on experience in AI/ML and data-driven solutions for real-time systems.
"""
EMAIL = "kkchaithanya2k0@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "http://www.linkedin.com/in/k-k-chaithanya",
    "GitHub": "https://github.com/kkchaithanya007",
}
PROJECTS = {
    "Object Detection Practice - Custom YOLO model implementation.": "https://github.com/kkchaithanya007/ObjectDetection/tree/master/ObjectDetectionOnePractice"
}

CERTIFICATES = {

    "Machine Learning with Python": "https://drive.google.com/file/d/1r1F2HSEipYNQBFtmYfoVDQSpvredzOmf/view?usp=sharing",
    "DDOS Project with Java":"https://drive.google.com/file/d/128xZfoHp1NJex-P36r7RSJZJdEDqSLCe/view?usp=sharing"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2)
with col1:
    st.image(profile_pic, width=230)
    

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA), gap="small")
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    col_list = f"<div class='center-align'><a href='{link}'>🔗 {platform}</a></div>"
    cols[index].markdown(col_list, unsafe_allow_html=True)

# --- About me ---
st.write('\n')
st.subheader("About me")
st.write(
    """
- ✔️ Hands-on experience in building and deploying computer vision and ML models.
- ✔️ Skilled in Python, Git, Streamlit, and automation of data workflows.
- ✔️ Good understanding of YOLO models, OpenCV, and real-time edge deployments.
- ✔️ Experienced in working with annotation tools like CVAT and managing training pipelines.
- ✔️ Quick learner with strong problem-solving skills and passion for AI/ML systems.
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👨‍💻 Programming: Python (OpenCV, Pandas, NumPy, Ultralytics), Bash, SQL.
- 📊 Data Visualization: Grafana, Matplotlib, Seaborn, MS Excel.
- 📚 Modeling: YOLOv8 (Object Detection), U-Net (Segmentation), CNN, EfficientNet, VGG, Transfer Learning.
- 💻 Designing: HTML, CSS, Streamlit.
- 🗄️ Databases: PostgreSQL, MySQL.
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Software Engineer | LivNSense GreenOps Pvt. Ltd.**")
st.write("10/2023 - 11/2024")
st.write(
    """
- ► Developed safety surveillance systems using Python, OpenCV, and PostgreSQL.
- ► Built data dashboards in Grafana and automated reporting pipelines.
- ► Supported AI/ML model integration, testing, and deployment for industrial safety projects.
- ► Worked on ADAS for Indian Railways using facial landmark detection.
- ► Deployed real-time monitoring solutions on edge devices for workplace safety.
- ► Handled dataset labeling, auto-labeling, and preprocessing using CVAT and FiftyOne.
"""
)

# --- Certifications ---
st.write('\n')
st.subheader("Certifications")
st.write("---")
certificates_list = list(CERTIFICATES.items())
cols = st.columns(2)
for index, (certificate, link) in enumerate(certificates_list):
    with cols[index % 2]:
        st.write(f"🥇 [{certificate}]({link})")

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"🎯 [{project}]({link})")
