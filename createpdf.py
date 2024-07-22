import PyPDF2
import pandas as pd

# Open the PDF file
with open("DataSciencePython.pdf", "rb") as file:
    # Create a PdfReader object
    pdf_reader = PyPDF2.PdfReader(file)
    
    # Extract text from the desired page (assuming page 4 based on your code)
    page_text = pdf_reader.pages[3].extract_text()

# Split the text into lines
lines = page_text.split('\n')

# Create a pandas DataFrame to hold the extracted data
df = pd.DataFrame(lines, columns=['Text'])

# Write the DataFrame to an Excel file
df.to_excel("extracted_text.xlsx", index=False)
