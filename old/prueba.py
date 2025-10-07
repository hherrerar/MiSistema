import openpyxl
import os

try:
    # Assuming 'my_excel_file.xlsx' is in the same directory as the script
    file_path = os.path.join(os.getcwd(), 'crud.xlsx') 
    workbook = openpyxl.load_workbook(file_path)
    print("Workbook loaded successfully.")
    # Further operations with the workbook
except openpyxl.utils.exceptions.InvalidFileException as e:
    print(f"Error loading workbook: {e}")
except FileNotFoundError:
    print("Error: The specified file was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
