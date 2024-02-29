import pretty_pdf
import time

# Benchmark time
start_time = time.time()

limit = 100000

def get_table_data():
    table_rows = ""
    for i in range(limit):
        table_rows += "<tr>"
        for j in range(6):
            table_rows += f"<td>Data {i + 1}-{j + 1}</td>"
        table_rows += "</tr>"
    return table_rows

if __name__ == "__main__":
    # Benchmark time
    print("Process started at:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time)))

    # PDF
    filepath = "download/" + str(start_time) + ".pdf"
    title = "Generate PDF using Python with WeasyPrint"
    header = ["ID", "COLUMN 2", "COLUMN 3", "COLUMN 4", "COLUMN 5", "COLUMN 6"]
    data = get_table_data() 
    pretty_pdf.generate_pdf(filepath, title, header, data)

    # Benchmark time
    end_time = time.time()
    print("Process ended at:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time)))
    elapsed_time = end_time - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    print(f"Total elapsed time: {minutes} min {seconds} seconds")
