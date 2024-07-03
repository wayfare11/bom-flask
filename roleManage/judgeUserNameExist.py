from connectMysql.getConnect import get_database_connection

def judge_user_name_exist(username):
    con = get_database_connection()
    try:
        with con.cursor() as cursor:
            sql = "SELECT * FROM t_user WHERE username = %s"
            cursor.execute(sql, (username,))
            # result = cursor.fetchall()
            return cursor.rowcount
    except Exception as e:
        print(e)

    finally:
        con.close()