from connectMysql.getConnect import get_database_connection
from flask import jsonify

def get_id_except_list(id, materialCode: str, Name: str):
    try:
        con = get_database_connection()
        with con.cursor() as cursor:
            # 使用参数化查询构建 SQL 查询，避免 SQL 注入风险
            sql = "SELECT * FROM components WHERE id!= %s"
            params = [id]

            if materialCode.strip() != "":
                sql += " AND materialCode LIKE %s"
                params.append(f"%{materialCode}%")

            if Name.strip() != "":
                sql += " AND Name LIKE %s"
                params.append(f"%{Name}%")

            cursor.execute(sql, tuple(params))
            data = cursor.fetchall()

            # 在每行数据的第一列添加一个数据
            all_list_data_index = [(i+1,) + row for i, row in enumerate(data)]

            # 转换为指定的 key-value 形式
            json_data = []
            for item in all_list_data_index:
                json_data.append({
                    "index": item[0],
                    "id": item[1],

                    "subset": item[13],

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
                })

            # 返回带有排序列的合并后的数据
            return jsonify(json_data)

    except Exception as e:
        # 添加适当的异常处理逻辑，这里只是简单地打印异常信息
        print(f"An error occurred: {e}")
        # 返回适当的错误信息给前端
        return jsonify({"error": "An error occurred while fetching data from the server"})

    finally:
        con.close()

def get_id_except_from_database(data):
    id = data.get("id")
    materialCode = data.get("materialCode")
    Name = data.get("Name")

    print("id:", id)
    print("materialCode:", materialCode)
    
    return get_id_except_list(id, materialCode, Name)