from connectMysql.getConnect import get_database_connection

def delete_component_from_database(id_to_delete):

    failed_deletions = []  # 用于记录删除失败的 ID
    try:
        con = get_database_connection()
        # 创建游标对象
        with con.cursor() as cursor:
            # 执行删除操作
            sql = "DELETE FROM components WHERE id = %s"
            cursor.execute(sql, (id_to_delete,))
            con.commit()  # 提交事务
            if cursor.rowcount > 0:
                return True  # 删除成功
            else:
                failed_deletions.append(id_to_delete)  # 记录删除失败的 ID
                return False  # 删除失败

    finally:
        con.close()  # 关闭数据库连接
        if failed_deletions:
            print(f"以下 ID 删除失败：{failed_deletions}")

