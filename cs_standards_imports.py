import os
import pandas as pd
from django.core.wsgi import get_wsgi_application

# Load the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lesson_management.settings')
application = get_wsgi_application()

from lesson_manage.models import CSStandard  # Replace 'db' with the name of your Django app

# Path to the spreadsheet
file_path = "tedSample.xlsx"

# Load the spreadsheet
excel_data = pd.ExcelFile(file_path)
standards_sheet = excel_data.parse('List of CS Standards')  # Replace with the actual sheet name

# Inspect the sheet structure to extract relevant data
print(standards_sheet.head())  # Optional: Print to ensure data is loaded correctly

# Loop through the rows and add standards to the database
for index, row in standards_sheet.iterrows():
    try:
        # Replace column names with actual column headers from your spreadsheet
        standard = str(row['Standard']) if not pd.isna(row['Standard']) else None
        grade = str(row['Grade']) if not pd.isna(row['Grade']) else None
        strand = str(row['Strand']) if not pd.isna(row['Strand']) else None

        # Skip rows with empty or null standard values
        if not standard:
            print(f"Skipping row {index}: 'Standard' field is empty or null.")
            continue

        # Add to the database
        cs_standard, created = CSStandard.objects.get_or_create(
            standard=standard,
            grade=grade,
            strand=strand
        )
        if created:
            print(f"Added new standard: {cs_standard}")
        else:
            print(f"Standard already exists: {cs_standard}")
    except KeyError as e:
        print(f"Missing column in row {index}: {e}")
    except Exception as e:
        print(f"Error processing row {index}: {e}")
