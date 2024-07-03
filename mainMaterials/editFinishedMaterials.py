from connectMysql.getConnect import get_database_connection
from mainMaterials.finishedType import DandaoMainMaterialType, YinliuMainMaterialType

def edit_dandao_finished_materials(listType: DandaoMainMaterialType, id):
    try:
        con = get_database_connection()
        cursor = con.cursor()
        sql = "UPDATE bdc_dandao SET MaterialCode=%s, fileCode=%s, Name=%s, ProductSpecifications=%s, Version=%s, ProductCode=%s, dandaoDiameter=%s, dandaoLength=%s, drainageMethod=%s, dandaoHeadStyle=%s, dandaoConfigurationCode=%s"
        sql += " WHERE id=%s"
        cursor.execute(sql, (listType.MaterialCode, listType.fileCode, listType.Name, listType.ProductSpecifications, listType.Version, listType.ProductCode, listType.dandaoDiameter, listType.dandaoLength, listType.drainageMethod, listType.dandaoHeadStyle, listType.dandaoConfigurationCode, id))
        con.commit()
        return cursor.rowcount
    except Exception as e:
        print(e)
        return 0
    finally:
        cursor.close()
        con.close()



def edit_yinliu_finished_materials(listType: YinliuMainMaterialType, id):
    try:
        con = get_database_connection()
        cursor = con.cursor()
        sql = "UPDATE dc_yinliu SET MaterialCode=%s, fileCode=%s, Name=%s, ProductSpecifications=%s, Version=%s, ProductCode=%s, yinliuDiameter=%s, yinliuLength=%s, yinliuLockStyle=%s, yinliuHeadStyle=%s, yinliuConfigurationCode=%s"
        sql += " WHERE id=%s"
        cursor.execute(sql, (listType.MaterialCode, listType.fileCode, listType.Name, listType.ProductSpecifications, listType.Version, listType.ProductCode, listType.yinliuDiameter, listType.yinliuLength, listType.yinliuLockStyle, listType.yinliuHeadStyle, listType.yinliuConfigurationCode, id))
        con.commit()
        return cursor.rowcount
    except Exception as e:
        print(e)
        return 0
    finally:
        cursor.close()
        con.close()

def edit_finished_materials(data):
    if data['ProductCode'] == "DC":
        listType = YinliuMainMaterialType(
            MaterialCode = data['MaterialCode'],
            fileCode = data['fileCode'],
            Name = data['Name'],
            ProductSpecifications = data['ProductSpecifications'],
            Version = data['Version'],
            ProductCode = data['ProductCode'],
            yinliuDiameter = data['yinliuDiameter'],
            yinliuLength = data['yinliuLength'],
            yinliuLockStyle = data['yinliuLockStyle'],
            yinliuHeadStyle = data['yinliuHeadStyle'],
            yinliuConfigurationCode = data['yinliuConfigurationCode']
        )
        return edit_yinliu_finished_materials(listType, data['id'])
    else:
        listType = DandaoMainMaterialType(
            MaterialCode = data['MaterialCode'],
            fileCode = data['fileCode'],
            Name = data['Name'],
            ProductSpecifications = data['ProductSpecifications'],
            Version = data['Version'],
            ProductCode = data['ProductCode'],
            dandaoDiameter = data['dandaoDiameter'],
            dandaoLength = data['dandaoLength'],
            drainageMethod = data['drainageMethod'],
            dandaoHeadStyle = data['dandaoHeadStyle'],
            dandaoConfigurationCode = data['dandaoConfigurationCode']
        )
        return edit_dandao_finished_materials(listType, data['id'])
