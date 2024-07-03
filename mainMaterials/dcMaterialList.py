from connectMysql.getConnect import get_database_connection
from flask import jsonify

def get_dc_list_data(yinliuDiameter: str, yinliuLength: str, yinliuLockStyle: str, yinliuHeadStyle: str, yinliuConfigurationCode: str):

    try:
        con = get_database_connection()
        with con.cursor() as cursor:

            # 选择 dc_yinliu 表的数据
            sql_dc_yinliu = "SELECT * FROM dc_yinliu WHERE 1=1"

            # 添加条件
            if yinliuDiameter.strip() != '':
                sql_dc_yinliu += " AND yinliuDiameter = '" + yinliuDiameter + "'"
            if yinliuLength.strip() != '':
                sql_dc_yinliu += " AND yinliuLength = '" + yinliuLength + "'"
            if yinliuLockStyle.strip() != '':
                sql_dc_yinliu += " AND yinliuLockStyle = '" + yinliuLockStyle + "'"
            if yinliuHeadStyle.strip() != '':
                sql_dc_yinliu += " AND yinliuHeadStyle = '" + yinliuHeadStyle + "'"
            if yinliuConfigurationCode.strip() != '':
                sql_dc_yinliu += " AND yinliuConfigurationCode = '" + yinliuConfigurationCode + "'"

            cursor.execute(sql_dc_yinliu)
            dc_yinliu_data = cursor.fetchall()

            # 在每行数据的第一列添加一个数据
            all_list_data_index = [(i+1,) + row for i, row in enumerate(dc_yinliu_data)]

            print(len(all_list_data_index))

            # 转换为指定的 key-value 形式
            json_data = []
            for item in all_list_data_index:
                json_data.append({
                    "index": item[0],
                    "id": item[1],
                    "MaterialCode": item[2],
                    "fileCode": item[3],
                    "Name": item[4],
                    "ProductSpecifications": item[5],
                    "Version": item[6],
                    "ProductCode": item[7],
                    "yinliuDiameter" : item[8],
                    "yinliuLength" : item[9],
                    "yinliuLockStyle": item[10],
                    "yinliuHeadStyle": item[11],
                    "yinliuConfigurationCode": item[12],
                })

            # 返回带有排序列的合并后的数据
            return jsonify(json_data)

    finally:
        con.close()
