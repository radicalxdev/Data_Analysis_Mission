# Necessary imports
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure the generative AI with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Print the API key being used (for verification purposes)
print("Using API Key:", os.getenv("GOOGLE_API_KEY")) 

# Prompt to be used for generating SQL queries
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    You will purely return the SQL query, and omit everything else, like ```, or the word sql
    The SQL database has the name EMPLOYEE and has the following columns - 
    ID, NAME, SALARY, AGE, GENDER, DESIGNATION, WORKING_HOURS, MONTHLY_LUNCH_BILL, BONUS
    \n\nFor example,\nExample 1 - Retrieve all employees
    the SQL command will be something like this SELECT * FROM EMPLOYEE;
    \nExample 2 - Retrieve employees with a specific salary range
    the SQL command will be something like this SELECT * FROM EMPLOYEE
    WHERE SALARY BETWEEN 50000 AND 70000;
    """
]

def get_gemini_response(question):
    """
    Function to get the response from the Gemini model for a given question.
    
    Your Steps:
    1. Initialize the GenerativeModel with the appropriate model name.
       Hint: Use genai.GenerativeModel() with the model name as "gemini-pro".
    2. Generate content by providing the combined prompt and question to the model's generate_content() method.
       Hint: Use response = model.generate_content([prompt[0], question]).
    3. Return the generated SQL query text from the response.
    
    Example for generating content:
    ```
    response = model.generate_content([prompt[0], question])
    return response.text
    ```
    """
    # Step 1: Initialize the GenerativeModel
    model = None  # Replace None with the correct initialization code.
    
    # Step 2: Generate content by providing the combined prompt and question
    response = None  # Replace None with the correct code to generate content.
    
    # Step 3: Return the generated SQL query text
    return None  # Replace None with the correct code to return the response text.

# Example usage
if __name__ == "__main__":
    question = "Retrieve employees with a salary greater than 60000"
    sql_query = get_gemini_response(question)
    print("Generated SQL Query:", sql_query)
