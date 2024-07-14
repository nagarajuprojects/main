import streamlit as st
import pandas as pd
import plotly.express as px
from docx import Document

CORRECT_USER_ID = "Admin"
CORRECT_PASSWORD = "123"

# Page configuration should be set before any Streamlit elements are created
st.set_page_config(
    page_title="Operations",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# Inject custom CSS to set the background color
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff;
    }
    .css-18e3th9 {
        background-color: #f0f8ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to display the main content after login
def display_main_content():
    # Load the primary CSV file
    try:
        df = pd.read_csv("inputfile.csv")
    except FileNotFoundError:
        st.error("The file 'inputfile.csv' was not found.")
        return

    # Load the secondary CSV file
    try:
        df1 = pd.read_csv("inputfile1.csv")
    except FileNotFoundError:
        st.warning("The file 'inputfile1.csv' was not found. Proceeding with only 'inputfile.csv'.")
        df1 = pd.DataFrame()  # Empty DataFrame if the file is not found

    # Check if the necessary columns exist
    if 'UserId' not in df.columns:
        st.error("The column 'UserId' is missing from 'inputfile.csv'.")
        return
    if not df1.empty and 'Userid' not in df1.columns:
        st.error("The column 'Userid' is missing from 'inputfile1.csv'.")
        return

    # Perform a left join if the secondary DataFrame is not empty
    if not df1.empty:
        df_merged = pd.merge(df, df1, left_on='UserId', right_on='Userid', how='left')
    else:
        df_merged = df

    st.write(df_merged)

    df_merged['Date'] = pd.to_datetime(df_merged['CreationDate']).dt.date
    df1_copy = df_merged.copy()

    # Group by UserId, Date, and Operation to count occurrences
    summary_df = df1_copy.groupby(['Fullname','UserId', 'Date', 'Operation']).size().reset_index(name='Count of Operations')

    final_summary_df = summary_df.groupby('Fullname').agg({
        'UserId':'first',
        'Date': 'first',
        'Operation': 'first',
        'Count of Operations': 'sum'
    }).reset_index()

    st.subheader("Operation Count by UserId, Date, and Operation")
    st.table(final_summary_df[['Fullname','UserId', 'Date', 'Operation', 'Count of Operations']])

    # Sidebar filters for Operation and CreationDate
    st.sidebar.header("Filters")
    selected_operation = st.sidebar.multiselect("Select Operation(s)", df_merged["Operation"].unique())
    selected_dates = st.sidebar.multiselect("Select Date(s)", df_merged["CreationDate"].unique())

    # Apply filters to create filtered DataFrame
    if selected_operation:
        df_merged = df_merged[df_merged['Operation'].isin(selected_operation)]
    if selected_dates:
        df_merged = df_merged[df_merged['CreationDate'].isin(selected_dates)]

    # Group by Date to count occurrences of Operation
    count_by_date = df_merged.groupby('Date').size().reset_index(name='Count of Operations')

    # Plotting bar chart for Count of Operations by CreationDate
    st.subheader("Count of Operations by Creation Date")
    fig_bar = px.bar(count_by_date, x='Date', y='Count of Operations', text='Count of Operations',
                     template='seaborn', title='Count of Operations by Creation Date')
    fig_bar.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig_bar.update_layout(xaxis_title='Creation Date', yaxis_title='Count of Operations')
    st.plotly_chart(fig_bar, use_container_width=True)

    # Group by Operation to sum RecordType
    record_type_summary = df_merged.groupby('Operation')['RecordType'].sum().reset_index()

    # Plotting pie chart for Sum of RecordType by Operation
    st.subheader("Sum of RecordType by Operation")
    fig_pie = px.pie(record_type_summary, values='RecordType', names='Operation', 
                     title='Sum of RecordType by Operation', hole=0.5)
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_pie, use_container_width=True)

# Function to read content from a DOCX file
def read_docx(file):
    document = Document(file)
    doc_text = []
    for para in document.paragraphs:
        doc_text.append(para.text)
    return '\n'.join(doc_text)

# Function to display another page content
def display_another_page():
    st.title("Course Syllabus")

    option = st.selectbox("Select a Course", ("Excel", "Power BI", "SQL"))

    if option == "Excel":
        content = read_docx("excel.docx")
    elif option == "Power BI":
        content = read_docx("powerbisyllabus.docx")
    elif option == "SQL":
        content = read_docx("sqlcoursesyllabus.docx")

    st.write(content)

# Initialize page state
if "loggedin" not in st.session_state:
    st.session_state.loggedin = False

# Check if logged_in query parameter is set to True
query_params = st.experimental_get_query_params()
if query_params.get('logged_in') == ['true']:
    st.session_state.loggedin = True

# Check if logged in and display content accordingly
if st.session_state.loggedin:
    # Navigation links in the sidebar
    st.sidebar.header("Navigation")

    # Determine which page is active based on query parameters
    is_page_main = query_params.get('page', ['main'])[0] == 'main'
    is_page_another = query_params.get('page', ['main'])[0] == 'another'

    # Highlight the active button based on the current page
    if is_page_main:
        page1_button = st.sidebar.button("Page 1", key='page1_button', help="Go to Page 1", on_click=lambda: st.experimental_set_query_params(logged_in=True, page="main"))
        page2_button = st.sidebar.button("Page 2", key='page2_button', help="Go to Page 2", on_click=lambda: st.experimental_set_query_params(logged_in=True, page="another"))
    elif is_page_another:
        page1_button = st.sidebar.button("Page 1", key='page1_button', help="Go to Page 1", on_click=lambda: st.experimental_set_query_params(logged_in=True, page="main"))
        page2_button = st.sidebar.button("Page 2", key='page2_button', help="Go to Page 2", on_click=lambda: st.experimental_set_query_params(logged_in=True, page="another"))

    # Display the appropriate content based on the current page
    if is_page_main:
        display_main_content()
    elif is_page_another:
        display_another_page()
else:
    def login():
        if st.session_state.user_id == CORRECT_USER_ID and st.session_state.password == CORRECT_PASSWORD:
            st.session_state.loggedin = True
            st.experimental_set_query_params(logged_in=True, page="main")
        else:
            st.session_state.loggedin = False
            st.error("Invalid username or password")

    st.header("Login")
    st.text_input("User ID", key="user_id")
    st.text_input("Password", type="password", key="password")
    if st.button("Login"):
        login()
