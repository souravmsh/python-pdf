# Generate PDF using Python with WeasyPrint

This guide demonstrates how to generate a PDF using Python, specifically employing the WeasyPrint library. The PDF generated will include a page with a fixed header and dynamic data presented in a table format.

## Features

- **Fixed Header**: The PDF will contain a fixed header that remains consistent across all pages.
- **Dynamic Data Table**: The PDF will include a table presenting dynamic data.
- **WeasyPrint Package**: WeasyPrint, a powerful library for rendering HTML and CSS to PDF, is utilized for PDF generation.

## Installation Guide for WeasyPrint

To install WeasyPrint, follow these steps:

1. **Install Dependencies**: Before installing WeasyPrint, ensure that the necessary system-level dependencies are installed. These dependencies may vary based on your operating system. Refer to the [official WeasyPrint documentation](https://weasyprint.readthedocs.io/en/stable/install.html#) for detailed instructions.

2. **Install WeasyPrint**: You can install WeasyPrint using pip, Python's package installer. Run the following command in your terminal or command prompt:

    ```
    pip install WeasyPrint
    ```

3. **Verify Installation**: After installation, verify that WeasyPrint is correctly installed by importing it in a Python environment. Open a Python interpreter or a Python script and import WeasyPrint:

    ```python
    import weasyprint
    ```

    If no errors occur, WeasyPrint is successfully installed.

## How to Use

Refer to your Python script to generate the PDF. Ensure that you have the necessary data and HTML/CSS templates to generate the PDF according to your requirements.

Here's a basic example of how to use WeasyPrint to generate a PDF:

```python
from weasyprint import HTML

# Default title of the table
title  = "Generate PDF using Python with WeasyPrint"

# Get table header
header = get_table_head(["ID", "COLUMN 2", "COLUMN 3", "COLUMN 4", "COLUMN 5", "COLUMN 6"])

# Sample dynamic data with tr td
data   = get_table_data()

# Generate PDF
generate_pdf("download.pdf", title, header, data)