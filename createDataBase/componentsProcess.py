import openpyxl
import pandas as pd
from sqlalchemy import create_engine

def add_leading_zeros_to_string(input_string):
    numbers = input_string.split(',')
    formatted_numbers = [f"{int(num):02d}" for num in numbers]
    return ','.join(formatted_numbers)

# 打开Excel文件
workbook = openpyxl.load_workbook('C:/Users/WB-wangyu/Desktop/引流导管BOM小程序数据库.xlsx')

# 获取第一个sheet
sheet = workbook.worksheets[0]

# 获取所有合并单元格
merged_cells_ranges = sheet.merged_cells.ranges

# 创建DataFrame对象
table_component = pd.DataFrame(sheet.values)

# 将每个合并的单元格拆分开
for merged_range in merged_cells_ranges:
    min_row, min_col, max_row, max_col = merged_range.min_row, merged_range.min_col, merged_range.max_row, merged_range.max_col
    for row in range(min_row, max_row + 1):
        for col in range(min_col, max_col + 1):
            if row != min_row or col != min_col:
                table_component.iloc[row - 1, col - 1] = table_component.iloc[min_row - 1, min_col - 1]

# 关闭Excel文件
workbook.close()

# 创建DataFrame对象
# table_component = pd.DataFrame(data, columns=columns)

# 选择从第三行开始的数据
table_component = table_component.iloc[2:, :]

# 重置索引
table_component.reset_index(drop=True, inplace=True)

table_component.insert(0, 'id', range(1, len(table_component) + 1))

for i in range(len(table_component)):
    for j in range(13):
        if table_component.iloc[i,j] == None:
            table_component.iloc[i,j] = ""

# 将胆道直径修改为标准格式
dandaoDiameter = table_component.iloc[:,2].astype(str)
for i in range(len(dandaoDiameter)):
    if dandaoDiameter[i].strip() != '':
        dandaoDiameter[i] = add_leading_zeros_to_string(dandaoDiameter[i])
table_component.iloc[:,2] = dandaoDiameter

# 将引流直径修改为标准格式
yinliuDiameter = table_component.iloc[:,7].astype(str)
for i in range(len(yinliuDiameter)):
    if yinliuDiameter[i].strip() != '':
        yinliuDiameter[i] = add_leading_zeros_to_string(yinliuDiameter[i])
table_component.iloc[:,7] = yinliuDiameter

# 重置列名
columns = ['id', 'ProductCode', 'dandaoDiameter', 'dandaoLength', 'drainageMethod', 'dandaoHeadStyle', 'dandaoConfigurationCode',
           'yinliuDiameter', 'yinliuLength', 'yinliuLockStyle', 'yinliuHeadStyle', 'yinliuConfigurationCode', 'subset', 'majorCategory',
           'materialCode', 'drawingCode', 'Name', 'specification', 'material', 'color', 'numbers', 'unit', 'materialCategory', 'Note', 'perPrice', 'totalPrice']

table_component.columns = columns

table_component['totalPrice'] = round(table_component['perPrice'] * table_component['numbers'], 4)
table_component['totalPrice'] = table_component['totalPrice'].astype(float)
table_component['totalPrice'] = round(table_component['totalPrice'], 4)
table_component['totalPrice'] = table_component['totalPrice'].astype(str)

table_component = table_component.astype(str)

print(table_component)

# 创建 SQLAlchemy 引擎
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/yinliu')

# 将id列转换为整数类型
table_component['id'] = table_component['id'].astype(int)

table_component.to_sql('components', con=engine, if_exists='replace', index=False)