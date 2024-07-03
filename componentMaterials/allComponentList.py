from connectMysql.getConnect import get_database_connection
from flask import jsonify

def get_all_component_list_data(componentName: str, componentMaterialCode: str):

    try:
        con = get_database_connection()
        with con.cursor() as cursor:
            # 选择 bdc_dandao 表的数据
            sql_components = "SELECT * FROM components where 1=1"

            # 如果 componentName 不为空，则添加 Name 的条件
            if componentName.strip() != '':
                sql_components += " AND Name LIKE '%" + componentName + "%'"

            # 如果 componentMaterialCode 不为空，则添加 materialCode 的条件
            if componentMaterialCode.strip() != '':
                sql_components += " AND materialCode LIKE '%" + componentMaterialCode + "%'"

            cursor.execute(sql_components)
            component_data = cursor.fetchall()

            # 如果返回的数据为空，直接返回空数据
            if not component_data:
                return jsonify([])

            # 在每行数据的第一列添加一个数据
            all_list_data_index = [(i+1,) + row for i, row in enumerate(component_data)]

            # 转换为指定的 key-value 形式
            json_data = []
            for item in all_list_data_index:
                json_data.append({
                    "index": item[0],
                    "id": item[1],

                    "ProductCode": item[2],
                    "dandaoDiameter": item[3],
                    "dandaoLength": item[4],
                    "drainageMethod": item[5],
                    "dandaoHeadStyle": item[6],
                    "dandaoConfigurationCode": item[7],
                    "yinliuDiameter": item[8],
                    "yinliuLength": item[9],
                    "yinliuLockStyle": item[10],
                    "yinliuHeadStyle": item[11],
                    "yinliuConfigurationCode": item[12],

                    "subset": item[13],

                    "majorCategory": item[14],
                    "materialCode": item[15],
                    "drawingCode": item[16],
                    "Name": item[17],
                    "specification": item[18],
                    "material": item[19],
                    "color": item[20],
                    "numbers": item[21],
                    "unit": item[22],
                    "materialCategory": item[23],
                    "Note": item[24],
                    "perPrice": item[25],
                    "totalPrice": item[26],
                })

            # 返回带有排序列的合并后的数据
            return jsonify(json_data)

    finally:
        con.close()