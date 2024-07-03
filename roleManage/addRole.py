from connectMysql.getConnect import get_database_connection

def add_role(role_data):
    con = get_database_connection()
    try:
        cursor = con.cursor()
        sql = "INSERT INTO t_user (username, password, super_root, normal_root, add_data_permission, edit_data_permission, delete_data_permission) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (role_data['username'], role_data['password'], role_data['super_root'], role_data['normal_root'], role_data['add_data_permission'], role_data['edit_data_permission'], role_data['delete_data_permission']))
        con.commit()
        return cursor.rowcount
        
    except Exception as e:
        print(e)
        return 0
    finally:
        con.close()
