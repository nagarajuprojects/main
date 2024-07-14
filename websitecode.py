import streamlit as st
import pandas as pd
import plotly.express as px

CORRECT_USER_ID = "Admin"
CORRECT_PASSWORD = "123"

# Page configuration should be set before any Streamlit elements are created
st.set_page_config(
    page_title="Operations",
    page_icon="",
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

    # Plotting bar chart for
