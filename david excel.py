from openpyxl import load_workbook
import pandas as pd
import matplotlib.pyplot as plt

file_name='enter file name'
wb = load_workbook(file_name)
ws = wb.active
added = []


def funcx(current):
    global added
    global file_name
    gene_names = ws["F" + str(current)].value
    for row in range(current, 50):
        cur_check = ws["F" + str(row)].value
        cur_gene_name = ws["B" + str(row)].value
        if cur_check is None:
            break
        if cur_check == gene_names and cur_gene_name not in added:
            added.append(cur_gene_name)
            ws["O" + str(current)].value = (str(ws["O" + str(current)].value) + ", " + cur_gene_name)[5:]
            a = ws["O" + str(current)].value
            added.append(cur_gene_name)
    wb.save(file_name)


current = 1
for cell in ws['F']:
    print(current)
    if cell.value is None or cell.value == "Genes":
        added = []
        current += 1
    else:
        funcx(current)
        current += 1

names = []
numbers = []
for num, cell in enumerate(ws["O"]):
    if cell.value is not None:
        names.append(str(cell.value))
        numbers.append(ws["C" + str(num + 1)].value)

new_data = {'names': names, 'numbers': numbers}
df = pd.DataFrame.from_dict(new_data);
df
plt.barh(df.names, df.numbers)
plt.show()
