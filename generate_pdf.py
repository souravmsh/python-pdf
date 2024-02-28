from weasyprint import HTML

def get_table_head(columns): 
    table_head = ""
    for column in columns:
        table_head += f"<th>{column}</th>"
    return table_head

def generate_pdf(output_path, header, table_head, table_body): 

    colspan = len(table_head)
    table_head = get_table_head(table_head)

    HTML_CONTENT = f"""
    <html>
    <head>
        <style>
            table {{
                border-collapse: collapse;
                width: 100%;
                margin-top:height: .5in;
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
                    <th colspan="{ colspan }" style="text-align:center"><h1>{ header }</h1></th>
                </tr> 
                <tr>
                    { table_head }
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


def get_table_data():
    table_rows = ""
    for i in range(2000):
        table_rows += "<tr>"
        for j in range(6):
            table_rows += f"<td>Data {i + 1}-{j + 1}</td>"
        table_rows += "</tr>"
    return table_rows

if __name__ == "__main__":

    title  = "Generate PDF using Python with WeasyPrint"
    header = ["ID", "COLUMN 2", "COLUMN 3", "COLUMN 4", "COLUMN 5", "COLUMN 6"]
    data   = get_table_data()

    generate_pdf("download.pdf", title, header, data)
 