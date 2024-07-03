from connectMysql.getConnect import get_database_connection
from flask import jsonify

def get_all_list_data():

    try:
        con = get_database_connection()
        with con.cursor() as cursor:
            # 选择 bdc_dandao 表的数据
            sql_bdc_dandao = "SELECT * FROM bdc_dandao"
            cursor.execute(sql_bdc_dandao)
            bdc_dandao_data = cursor.fetchall()

            # 选择 dc_yinliu 表的数据
            sql_dc_yinliu = "SELECT * FROM dc_yinliu"
            cursor.execute(sql_dc_yinliu)
            dc_yinliu_data = cursor.fetchall()

            # 合并数据
            all_list_data = bdc_dandao_data + dc_yinliu_data

            # 在每行数据的第一列添加一个数据
            all_list_data_index = [(i+1,) + row for i, row in enumerate(all_list_data)]

            print(all_list_data_index[0])

            # 转换为指定的 key-value 形式
            json_data = []
            for item in all_list_data_index:
                if item[7] == "DC":
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
                elif item[7] == "BDC":
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
