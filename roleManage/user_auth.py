from flask import request, jsonify
from connectMysql.getConnect import get_database_connection

# 用户验证函数
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return jsonify({'message': '用户名和密码不能为空！'}), 401

    connection = get_database_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM t_user WHERE username = %s AND password = %s"
            cursor.execute(sql, (auth.username, auth.password))
            user = cursor.fetchone()
        if user:
            json_data = []
            json_data.append({
                "message": "登录成功！",
                "id": user[0],
                "username": user[1],
                "password": user[2],
                "super_root": user[3],
                "normal_root": user[4],
                "add_data_permission": user[5],
                "edit_data_permission": user[6],
                "delete_data_permission": user[7]
            })
            return jsonify(json_data), 200
        else:
            return jsonify({'message': '用户名或密码错误！'}), 401
    finally:
        connection.close()
