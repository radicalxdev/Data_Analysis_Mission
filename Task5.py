import streamlit as st
import pandas as pd
from Tasks.Task1 import get_gemini_response
from Tasks.Task2 import execute_sql_query
from Tasks.Task3 import plot_data
from Tasks.Task4 import download_link


# Predefined SQL commands
sql_commands = {
    "Retrieve all employees": "SELECT * FROM EMPLOYEE;",
    "Retrieve employees with a specific salary range": "SELECT * FROM EMPLOYEE WHERE SALARY BETWEEN 50000 AND 70000;",
    "High Salary Employees": "SELECT * FROM EMPLOYEE WHERE SALARY > 80000;",
    "Female Employees": "SELECT * FROM EMPLOYEE WHERE GENDER = 'Female';",
    "Young Employees (Age < 30)": "SELECT * FROM EMPLOYEE WHERE AGE < 30;",
    "Top 10 Working Hours": "SELECT * FROM EMPLOYEE ORDER BY WORKING_HOURS DESC LIMIT 10;",
    "Top 10 Monthly Lunch Bills": "SELECT * FROM EMPLOYEE ORDER BY MONTHLY_LUNCH_BILL DESC LIMIT 10;",
    "Employees in IT Department": "SELECT * FROM EMPLOYEE WHERE DEPARTMENT = 'IT';",
    "Senior Managers": "SELECT * FROM EMPLOYEE WHERE DESIGNATION = 'Senior Manager';",
    "Lowest Salary Employees": "SELECT * FROM EMPLOYEE ORDER BY SALARY ASC LIMIT 10;",
    "Employees with Bonus": "SELECT * FROM EMPLOYEE WHERE BONUS > 0;"
}

# Streamlit app configuration
st.set_page_config(page_title="I can Retrieve Any SQL query", layout="wide")

# Sidebar for input and predefined SQL commands
st.sidebar.title("Features")

# Ask question input
question = st.sidebar.text_input("Your Question:", key="input")
ask_question_button = st.sidebar.button("Ask SQL.AI")

# Dropdown menu for predefined SQL commands
selected_command = st.sidebar.selectbox("Select a predefined SQL command:", list(sql_commands.keys()))

# Button to execute the selected command
execute_command_button = st.sidebar.button("Execute Command")

# Widgets for custom search
st.sidebar.header("Custom Search Options")
selected_columns = st.sidebar.multiselect("Select Columns for Visualization:", ["SALARY", "AGE", "WORKING_HOURS", "BONUS"])
date_range = st.sidebar.date_input("Select Date Range:", [pd.to_datetime("2022-01-01"), pd.to_datetime("2022-12-31")])

st.sidebar.header("Download CSV")

# Main content area for data plot
st.title("SQL.AI - Retrieve SQL Data")

if ask_question_button:
    response = get_gemini_response(question)
    st.subheader("SQL.AI's Response:")
    st.info(response)

    if "Error executing SQL query" in response:
        st.error(response)
    else:
        try:
            # Step 1: Execute the SQL query and fetch data
            data = execute_sql_query(response, "company.db")

            if "Error executing SQL query" in data:
                st.error(data)
            else:
                # Display the retrieved data in a table
                st.subheader("All Data:")
                st.table(data)

                if data:
                    columns = ["ID", "NAME", "SALARY", "AGE", "GENDER", "DESIGNATION", "WORKING_HOURS", "MONTHLY_LUNCH_BILL", "BONUS"]
                    df = pd.DataFrame(data, columns=columns)

                    # Print the DataFrame
                    st.write("DataFrame:", df)

                    # Step 2: Plot data
                    plot_data(df)

                    # Step 3: Generate download link for CSV
                    st.markdown(download_link(df), unsafe_allow_html=True)
                else:
                    st.warning("No data to plot.")
        except Exception as e:
            st.error(f"Error processing data: {e}")

elif execute_command_button:
    if selected_command in sql_commands:
        sql_query = sql_commands[selected_command]
        response = f"Executing predefined SQL command: {selected_command}"
    else:
        response = get_gemini_response(question)
        sql_query = response

    st.subheader("Gemini's Response:")
    st.info(response)

    if "Error executing SQL query" in response:
        st.error(response)
    else:
        try:
            # Step 1: Execute the SQL query and fetch data
            data = execute_sql_query(sql_query, "company.db")

            if "Error executing SQL query" in data:
                st.error(data)
            else:
                # Display the retrieved data in a table
                st.subheader("All Data:")
                st.table(data)

                if data:
                    columns = ["ID", "NAME", "SALARY", "AGE", "GENDER", "DESIGNATION", "WORKING_HOURS", "MONTHLY_LUNCH_BILL", "BONUS"]
                    df = pd.DataFrame(data, columns=columns)

                    # Print the DataFrame
                    st.write("DataFrame:", df)

                    # Step 2: Plot data
                    plot_data(df)

                    # Step 3: Generate download link for CSV
                    st.markdown(download_link(df), unsafe_allow_html=True)
                else:
                    st.warning("No data to plot.")
        except Exception as e:
            st.error(f"Error processing data: {e}")

# Display a default message when no command is executed
st.info("Enter a question or select a predefined SQL command to execute.")
