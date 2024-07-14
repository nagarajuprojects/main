import streamlit as st
from streamlit_option_menu import option_menu
import docx

# Function to read content from docx files
def read_docx(excel.docx):
    doc = docx.Document("https://github.com/nagarajuprojects/main/tree/main")
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return "\n".join(full_text)

# Page configuration
st.set_page_config(
    page_title="BI 2 AI Technologies Training",
    page_icon="pbiexellogo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar for navigation
with st.sidebar:
    page_selection = option_menu(
        "Navigation", 
        ["Home", "Courses", "Contact"],
        icons=["house", "book", "envelope"],
        menu_icon="cast", 
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#f0f2f6"},
            "icon": {"color": "blue", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#0c5a8c"},
        }
    )

# Home Page
if page_selection == "Home":
    st.title("Welcome to BI 2 AI Technologies Training")
    st.image("pbiexellogo.png", width=250)  # Replace with your logo URL
    st.header("Learn Power BI, SQL, Excel, VBA")
    st.write("""
        We offer comprehensive training in Power BI, SQL, Excel, and VBA. Our courses are designed to help you master these tools and become proficient in data analysis and visualization. 
        Whether you are a beginner or looking to advance your skills, we have the right course for you.
    """)
    st.subheader("Why Choose Us?")
    st.write("""
        - Expert Instructors
        - Hands-on Training
        - Comprehensive Curriculum
        - Flexible Schedule
        - Certification
    """)

# Courses Page
elif page_selection == "Courses":
    st.title("Our Courses @ ₹15000")
    course_selection = st.selectbox("Select a Course", ["Excel", "Power BI", "SQL"])

    if course_selection == "Excel":
        st.title("Excel Course Content")
        excel_content = read_docx("excel.docx")
        st.write(excel_content)

    elif course_selection == "Power BI":
        st.title("Power BI Course Content")
        power_bi_content = read_docx("powerbisyllabus.docx")
        st.write(power_bi_content)

    elif course_selection == "SQL":
        st.title("SQL Course Content")
        sql_content = read_docx("sqlcoursesyllabus.docx")
        st.write(sql_content)

# Content Page
elif page_selection == "Content":
    st.title("Content Page")
    st.write("This page displays content from selected courses.")

# Contact Page
elif page_selection == "Contact":
    st.title("Contact Us")
    st.write("We'd love to hear from you! Fill out the form below to get in touch.")
    
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write(f"Thank you {name}! We have received your message and will get back to you at {email}.")

# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #f0f2f6;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
    <p>© 2024 Power BI, Excel, SQL & Cloud Trainings. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)
