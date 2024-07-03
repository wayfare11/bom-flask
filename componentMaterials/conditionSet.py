from connectMysql.getConnect import get_database_connection
from componentMaterials.componentType import ComponentUpdateConditionType

def conditionSet(listType: ComponentUpdateConditionType, id):
    try:
        con = get_database_connection()
        cursor = con.cursor()
        sql = "update components set ProductCode=%s,yinliuDiameter=%s,yinliuLength=%s,yinliuLockStyle=%s,yinliuHeadStyle=%s,yinliuConfigurationCode=%s,dandaoDiameter=%s,dandaoLength=%s,drainageMethod=%s,dandaoHeadStyle=%s,dandaoConfigurationCode=%s"
        sql += " where id=%s"

        cursor.execute(
            sql,
            (
                listType.ProductCode,
                listType.yinliuDiameter,
                listType.yinliuLength,
                listType.yinliuLockStyle,
                listType.yinliuHeadStyle,
                listType.yinliuConfigurationCode,
                listType.dandaoDiameter,
                listType.dandaoLength,
                listType.drainageMethod,
                listType.dandaoHeadStyle,
                listType.dandaoConfigurationCode,
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


def condition_set_from_database(data):

    id = data['id']
    listType = ComponentUpdateConditionType(
        ProductCode=data['ProductCode'],
        yinliuDiameter=data['yinliuDiameter'],
        yinliuLength=data['yinliuLength'],
        yinliuLockStyle=data['yinliuLockStyle'],
        yinliuHeadStyle=data['yinliuHeadStyle'],
        yinliuConfigurationCode=data['yinliuConfigurationCode'],
        dandaoDiameter=data['dandaoDiameter'],
        dandaoLength=data['dandaoLength'],
        drainageMethod=data['drainageMethod'],
        dandaoHeadStyle=data['dandaoHeadStyle'],
        dandaoConfigurationCode=data['dandaoConfigurationCode'],
    )

    if conditionSet(listType, id) > 0:
        print("更新成功")
    else:
        print("更新失败")