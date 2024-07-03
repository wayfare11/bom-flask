from connectMysql.getConnect import get_database_connection
from flask import jsonify

def getRoleList(userName, superRoot):
    con = get_database_connection()
    try:
        with con.cursor() as cursor:
            sql = "SELECT * FROM t_user WHERE username LIKE %s"

            if superRoot == "true":
                cursor.execute(sql, ('%' + userName + '%',))

                role_data = cursor.fetchall()
            else:
                sql += " AND super_root = 0"
                cursor.execute(sql, ('%' + userName + '%',))
                role_data = cursor.fetchall()

            # 在每行数据的第一列添加一个数据
            role_data_index = [(i+1,) + row for i, row in enumerate(role_data)]

            json_data = []

            for item in role_data_index:
                json_data.append({
                    "index": item[0],
                    "id": item[1],
                    "username": item[2],
                    "password": item[3],
                    "super_root": item[4],
                    "normal_root": item[5],
                    "add_data_permission": item[6],
                    "edit_data_permission": item[7],
                    "delete_data_permission": item[8]
                })

            return jsonify(json_data)
    except Exception as e:
        print(e)
    finally:
        con.close()
