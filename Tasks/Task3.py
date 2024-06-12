# Necessary imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st

def plot_data(df):
    """
    Plots visualizations for numeric columns and gender distribution from the provided DataFrame.

    Your Steps:
    1. Convert the specified columns to numeric types, handling non-numeric values gracefully.
       Hint: Use df[numeric_columns].apply(pd.to_numeric, errors='coerce').
    2. Loop through each numeric column and create a visualization.
       a. For columns with 10 or fewer unique values, create a bar plot.
          Hint: Use sns.barplot() with appropriate parameters.
       b. For columns with more than 10 unique values, create a histogram with KDE.
          Hint: Use sns.histplot() with appropriate parameters.
    3. Display each plot in the Streamlit app using st.pyplot().
    4. Create and display a pie chart for gender distribution.
       Hint: Use df["GENDER"].value_counts() to get counts and plt.pie() to create the pie chart.
    
    Example for converting columns to numeric types:
    ```
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')
    ```
    """
    # Step 1: Convert the specified columns to numeric types
    numeric_columns = ["SALARY", "AGE", "WORKING_HOURS", "MONTHLY_LUNCH_BILL", "BONUS"]
    df[numeric_columns] = None  # Replace None with the correct conversion code.
    
    for column in numeric_columns:
        st.subheader(f"Visualization for {column}")

        if len(df[column].unique()) <= 10:
            # Step 2a: Create a bar plot for columns with 10 or fewer unique values
            fig = plt.figure() 
            sns.barplot(None)  # Replace None with the correct bar plot code.
            plt.xlabel("Employee Name")
            plt.ylabel(column)
        else:
            # Step 2b: Create a histogram with KDE for columns with more than 10 unique values
            fig = plt.figure() 
            sns.histplot(None)  # Replace None with the correct histogram code.
            plt.xlabel(column)
            plt.ylabel("Frequency")

        # Step 3: Display the plot in the Streamlit app
        st.pyplot(fig)
        plt.close(fig)

    st.subheader("Gender Distribution")
    # Step 4: Create and display a pie chart for gender distribution
    gender_counts = None  # Replace None with the correct value counts code.
    plt.pie(None)  # Replace None with the correct pie chart code.
    st.pyplot(plt)
