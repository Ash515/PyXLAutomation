import pandas as pd

# 1.Read in the two Excel files

file1 = pd.read_excel('C:\\Users\\ashwin-ts69\\Desktop\\PyExcelAuto\\file1.xlsx')
file2 = pd.read_excel('C:\\Users\\ashwin-ts69\\Desktop\\PyExcelAuto\\file2.xlsx')
merged_file = pd.concat([file1, file2], ignore_index=True)
merged_file.to_excel('merged_file.xlsx', index=False)


# 2.Read and Export as a XLfiles

df = pd.read_excel('C:\\Users\\ashwin-ts69\\Desktop\\PyExcelAuto\\merged_file.xlsx', sheet_name='Sheet1')
df.to_excel('new_filename.xlsx', index=False)
