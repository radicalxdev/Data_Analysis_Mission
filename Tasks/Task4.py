
# Necessary imports
import pandas as pd
import base64

def download_link(df, filename="data.csv", text="Download CSV"):
    """
    Generates a download link for a DataFrame as a CSV file.

    Your Steps:
    1. Convert the DataFrame to a CSV string.
       Hint: Use df.to_csv() with index=False to exclude row indices.
    2. Encode the CSV string to base64 to make it suitable for a data URL.
       Hint: Use base64.b64encode() to encode the string and decode() to convert it to a regular string.
    3. Create an HTML link with the base64-encoded CSV that can be used to download the file.
       Hint: Use an <a> tag with the href attribute set to a data URL containing the base64-encoded CSV.

    Example for converting DataFrame to CSV:
    ```
    csv = df.to_csv(index=False)
    ```
    """
    # Step 1: Convert the DataFrame to a CSV string
    csv = None  # Replace None with the correct conversion code.
    
    # Step 2: Encode the CSV string to base64
    b64 = None  # Replace None with the correct encoding code.
    
    # Step 3: Create an HTML link for downloading the CSV file
    href = None  # Replace None with the correct HTML link creation code.
    
    return href
