from connectMysql.getConnect import get_database_connection

def delete_finished_materials(productCode, id):
    try:
        con = get_database_connection()
        cursor = con.cursor()
        if productCode == "DC":
            cursor.execute("DELETE FROM dc_yinliu WHERE id = %s", (id,))
        else:
            cursor.execute("DELETE FROM bdc_dandao WHERE id = %s", (id,))
        con.commit()
        return cursor.rowcount
    except Exception as e:
        print(e)
        return 0
    finally:
        cursor.close()
