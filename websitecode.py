import streamlit as st
import requests
import io
from docx import Document
from streamlit_option_menu import option_menu

# Function to fetch content from docx file URL
def fetch_docx_content(docx_url):
    response = requests.get(docx_url)
    docx_file = io.BytesIO(response.content)
    doc = Document(docx_file)
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
        ["Home", "Courses", "Content", "Contact"],
        icons=["house", "book", "file-text", "envelope"],
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
    st.header("Power BI")
    st.write("""
        Learn to create interactive dashboards and reports with Power BI. Our course covers data modeling, DAX, and Power BI service.
        - **Duration**: 4 weeks
    """)
    st.header("SQL")
    st.write("""
        Master SQL for database management and data manipulation. Our course includes SQL queries, joins, subqueries, and database design.
        - **Duration**: 4 weeks
    """)
    st.header("Excel")
    st.write("""
        Become an Excel expert with our training. Learn advanced formulas, pivot tables, data analysis, and VBA for automation.
        - **Duration**: 3 weeks
    """)
    st.header("VBA")
    st.write("""
        Automate your Excel tasks with VBA. Our course covers VBA programming, macros, and creating custom functions.
        - **Duration**: 2 weeks
    """)

# Content Page
elif page_selection == "Content":
    st.title("Content")
    st.header("Excel Course Syllabus")
    excel_docx_url = "https://raw.githubusercontent.com/nagarajuprojects/main/excel.docx"
    excel_content = fetch_docx_content(excel_docx_url)
    st.write(excel_content)

    st.header("Power BI Syllabus")
    powerbi_docx_url = "https://raw.githubusercontent.com/nagarajuprojects/main/powerbisyllabus.docx"
    powerbi_content = fetch_docx_content(powerbi_docx_url)
    st.write(powerbi_content)

    st.header("SQL Course Syllabus")
    sql_docx_url = "https://raw.githubusercontent.com/nagarajuprojects/main/sqlcoursesyllabus.docx"
    sql_content = fetch_docx_content(sql_docx_url)
    st.write(sql_content)

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
