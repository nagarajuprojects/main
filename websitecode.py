import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Power BI, Excel, SQL & Cloud Trainings",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar for navigation
st.sidebar.title("Navigation")
pages = ["Home", "Courses", "Contact"]
page_selection = st.sidebar.radio("Go to", pages)

# Home Page
if page_selection == "Home":
    st.title("Welcome to Power BI, Excel, SQL & Cloud Trainings")
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
        - Duration: 4 weeks
    """)
    st.header("SQL")
    st.write("""
        Master SQL for database management and data manipulation. Our course includes SQL queries, joins, subqueries, and database design.
        - Duration: 4 weeks
    """)
    st.header("Excel")
    st.write("""
        Become an Excel expert with our training. Learn advanced formulas, pivot tables, data analysis, and VBA for automation.
        - Duration: 3 weeks
    """)
    st.header("VBA")
    st.write("""
        Automate your Excel tasks with VBA. Our course covers VBA programming, macros, and creating custom functions.
        - Duration: 2 weeks
    """)

# Contact Page

elif page_selection == "Contact":
    st.title("Contact Us")
    st.write("We'd love to hear from you! Fill out the form below to get in touch.")
    
    with st.form("contact_form"):
        name = st.text_input("Name", value="Chiranjeevi Kudipudi")
        email = st.text_input("Email", value="dnraju478@gmail.com")
        message = st.text_area("Message")
        mobile_number = st.text_input("Mobile Number", value="9948140217")
        
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
        background-color: #f1f1f1;
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
