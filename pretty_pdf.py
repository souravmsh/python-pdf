from weasyprint import HTML

def generate_pdf(output_path, title, header, table_body):
    def get_table_head(columns):
        table_head = ""
        for column in columns:
            table_head += f"<th>{column}</th>"
        return table_head

    table_head = get_table_head(header)
    colspan = len(header)

    HTML_CONTENT = f"""
    <html>
    <head>
        <style>
            table {{
                border-collapse: collapse;
                width: 100%;
            }}
            th, td {{
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
            }}
            @page {{
                size: letter;
                margin: 2mm
            }}
        </style>
    </head>
    <body>
        <table>
            <thead>
                <tr>
                    <th colspan="{colspan}" style="text-align:center"><h1>{title}</h1></th>
                </tr> 
                <tr>
                    {table_head}
                </tr> 
            </thead>
            <tbody>
                {table_body}
            </tbody>
        </table>
    </body>
    </html>
    """

    # Generate PDF from HTML content
    HTML(string=HTML_CONTENT).write_pdf(output_path)
