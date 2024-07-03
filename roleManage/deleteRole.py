from connectMysql.getConnect import get_database_connection

def delete_role(role_id):
    con = get_database_connection()
    try:
        with con.cursor() as cursor:
            sql = "DELETE FROM t_user WHERE id = %s"
            cursor.execute(sql, (role_id,))
            con.commit()
            return cursor.rowcount
        
    except Exception as e:
        print(e)
        return 0
    finally:
        con.close()