from docx.api import Document
from docx.shared import Inches
document = Document("C:\prog_questionmark\Discospect\Папка с говной\\test.docx")
string = "This is first column--this is second column with some excessive information wich would be related to given topic--and this is the last column with some more info\nThis is first column--this is second column with some excessive information wich would be related to given topic--and this is the last column with some more info"
rows = string.split("\n")
data = []
for value in rows:
    data.append(value.split("--"))
print(data)
print(len(rows))
print(len(data[0]))
table = document.add_table(rows = len(rows), cols = len(data[0]))
# for id, name in data:
  
#     # Adding a row and then adding data in it.
#     row = table.add_row().cells
#     # Converting id to string as table can only take string input
#     row[0].text = str(id)
#     row[1].text = name
for value in data:
    row = table.add_row().cells
    for i in range(len(value)):
        row[i].text = value[i]
# table.style = "Colorful List"

document.save("C:\prog_questionmark\Discospect\Папка с говной\\test.docx")