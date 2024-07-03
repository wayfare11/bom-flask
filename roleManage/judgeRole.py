from flask import Flask, jsonify
from connectMysql.getConnect import get_database_connection

app = Flask(__name__)


def judgeRole(role_id, permission_operation):
    # 连接数据库
    con = get_database_connection()
    try:
        with con.cursor() as cursor:
            sql = "SELECT * FROM t_user WHERE id = %s"
            cursor.execute(sql, (role_id,))
            result = cursor.fetchone()

            # 定义键列表
            keys = [
                "id",
                "username",
                "password",
                "super_root",
                "normal_root",
                "add_data_permission",
                "edit_data_permission",
                "delete_data_permission",
            ]

            # 将结果转换为字典
            result_dict = {keys[i]: result[i] for i in range(len(keys))}

            if result_dict[f"{permission_operation}"] == 1:
                return "1"
            else:
                return "0"
    except Exception as e:
        print("查询失败:", e)
        return jsonify({"error": "Query failed"}), 500
    finally:
        con.close()
