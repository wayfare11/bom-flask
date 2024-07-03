from connectMysql.getConnect import get_database_connection
from flask import jsonify

def add_logs(logs_data):

    con = get_database_connection()
    try:
        with con.cursor() as cursor:
            add_log_query = (
                        "INSERT INTO operation_logs (username, user_role, action, content, timestamp) "
                        "VALUES (%s, %s, %s, %s, %s)"
                    )
            
            log_values = (
                logs_data['user_name'],
                logs_data['user_identity'],
                logs_data['operation_type'],
                logs_data['operation_content'],
                logs_data['operation_time']
            )

            cursor.execute(add_log_query, log_values)
            con.commit()
            return cursor.rowcount
    except Exception as e:
        print(e)
        return 0
    finally:
        con.close()


def get_logs_list(user_name, user_identity, operation_type):
    con = get_database_connection()
    try:
        with con.cursor() as cursor:
            query = "SELECT * FROM operation_logs WHERE 1=1"
            params = []

            if user_name:
                query += " AND username = %s"
                params.append(user_name)
            if user_identity:
                query += " AND user_role = %s"
                params.append(user_identity)
            if operation_type:
                query += " AND action = %s"
                params.append(operation_type)
            
            cursor.execute(query, params)
            logs = cursor.fetchall()

            # 添加键值对
            formatted_logs = [
                {
                    "log_id": log[0],
                    "username": log[1],
                    "user_role": log[2],
                    "action": log[3],
                    "content": log[4],
                    "timestamp": log[5].strftime('%Y-%m-%d %H:%M:%S')
                }
                for log in logs
            ]


            cursor.close()
            return jsonify(formatted_logs), 200
    except Exception as e:
        print(e)
        return jsonify([]), 500
    finally:
        con.close()
