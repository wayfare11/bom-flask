from connectMysql.getConnect import get_database_connection


def sonSet(id, son_set):
    try:
        con = get_database_connection()
        cursor = con.cursor()
        sql = "update components set subset=%s"
        sql += " where id=%s"

        cursor.execute(
            sql,
            (
                son_set,
                id,
            ),
        )
        con.commit()
        return cursor.rowcount
    except Exception as e:
        if con is not None:
            con.rollback()
        print(e)
        return 0
    finally:
        if con is not None:
            con.close()
