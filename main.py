import pretty_pdf

def get_table_data():
    table_rows = ""
    for i in range(2000):
        table_rows += "<tr>"
        for j in range(6):
            table_rows += f"<td>Data {i + 1}-{j + 1}</td>"
        table_rows += "</tr>"
    return table_rows

if __name__ == "__main__":
    title = "Generate PDF using Python with WeasyPrint"
    header = ["ID", "COLUMN 2", "COLUMN 3", "COLUMN 4", "COLUMN 5", "COLUMN 6"]
    data = get_table_data()

    pretty_pdf.generate_pdf("download.pdf", title, header, data)
