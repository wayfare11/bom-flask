from connectMysql.getConnect import get_database_connection
from flask import jsonify

def get_bdc_list_data(dandaoDiameter: str, dandaoLength: str, drainageMethod: str, dandaoHeadStyle: str, dandaoConfigurationCode:str):

    try:
        con = get_database_connection()
        with con.cursor() as cursor:
            # 选择 dc_yinliu 表的数据
            sql_bdc_dandao = "SELECT * FROM bdc_dandao WHERE 1=1"

            if dandaoDiameter.strip() != '':
                sql_bdc_dandao += " AND dandaoDiameter = '" + dandaoDiameter + "'"
            if dandaoLength.strip() != '':
                sql_bdc_dandao += " AND dandaoLength = '" + dandaoLength + "'"
            if drainageMethod.strip() != '':
                sql_bdc_dandao += " AND drainageMethod = '" + drainageMethod + "'"
            if dandaoHeadStyle.strip() != '':
                sql_bdc_dandao += " AND dandaoHeadStyle = '" + dandaoHeadStyle + "'"
            if dandaoConfigurationCode.strip() != '':
                sql_bdc_dandao += " AND dandaoConfigurationCode = '" + dandaoConfigurationCode + "'"

            cursor.execute(sql_bdc_dandao)
            bdc_dandao_data = cursor.fetchall()

            # 在每行数据的第一列添加一个数据
            all_list_data_index = [(i+1,) + row for i, row in enumerate(bdc_dandao_data)]

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
                    "dandaoDiameter": item[8],
                    "dandaoLength": item[9],
                    "drainageMethod": item[10],
                    "dandaoHeadStyle": item[11],
                    "dandaoConfigurationCode": item[12],
                })

            # 返回带有排序列的合并后的数据
            return jsonify(json_data)

    finally:
        con.close()
