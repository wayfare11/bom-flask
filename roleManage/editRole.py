from connectMysql.getConnect import get_database_connection

def edit_role(role_data):
    con = get_database_connection()

    print(role_data['normal_root'])
    print('id', role_data['role_id'])

    try:
        with con.cursor() as cursor:
            sql = "UPDATE t_user SET username = %s, password = %s, super_root = %s, normal_root = %s, add_data_permission = %s, edit_data_permission = %s, delete_data_permission = %s WHERE id = %s"
            cursor.execute(sql, (role_data['username'], role_data['password'], role_data['super_root'], role_data['normal_root'], role_data['add_data_permission'], role_data['edit_data_permission'], role_data['delete_data_permission'], role_data['role_id']))
            con.commit()
            return cursor.rowcount
    except Exception as e:
        print(e)
        return 0
    finally:
        con.close()
