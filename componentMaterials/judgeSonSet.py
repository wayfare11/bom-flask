from connectMysql.getConnect import get_database_connection

def searchByMaterialCode(materialCode):
    try:
        con = get_database_connection()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM components WHERE materialCode = %s", (materialCode))

        result = cursor.fetchall()

        return result
    except Exception as e:
        print(e)
        return 0
    finally:
        con.close()


def judge_son_set_exist(parent_set, son_set):

    if son_set == parent_set:
        return True
    else:
        result = searchByMaterialCode(son_set)
        if result:
            for row in result:
                # print('row',row)
                # print('row[14]',row[14])
                # print('parent_set',parent_set)
                if row[14] == parent_set:
                    return True
                else:
                    if row[12] != '':
                        for son_set_son in row[12].split(','):
                            return judge_son_set_exist(parent_set, son_set_son)

        return False