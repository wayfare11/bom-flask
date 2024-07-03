from connectMysql.getConnect import get_database_connection
from mainMaterials.finishedType import DandaoMainMaterialType, YinliuMainMaterialType

def add_dandao_main_material(listType: DandaoMainMaterialType):
    try:
        con = get_database_connection()
        cursor = con.cursor()
        sql = f"insert into bdc_dandao values(null,'{listType.MaterialCode}','{listType.fileCode}','{listType.Name}','{listType.ProductSpecifications}','{listType.Version}','{listType.ProductCode}','{listType.dandaoDiameter}','{listType.dandaoLength}','{listType.drainageMethod}','{listType.dandaoHeadStyle}','{listType.dandaoConfigurationCode}')"
        cursor.execute(sql)
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

def add_yinliu_main_material(listType: YinliuMainMaterialType):
    try:
        con = get_database_connection()
        cursor = con.cursor()
        sql = f"insert into dc_yinliu values(null,'{listType.MaterialCode}','{listType.fileCode}','{listType.Name}','{listType.ProductSpecifications}','{listType.Version}','{listType.ProductCode}','{listType.yinliuDiameter}','{listType.yinliuLength}','{listType.yinliuLockStyle}','{listType.yinliuHeadStyle}','{listType.yinliuConfigurationCode}')"
        cursor.execute(sql)
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

def add_main_material(data):

    ProductCode = data['ProductCode']

    if ProductCode == 'DC':
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
        return add_yinliu_main_material(listType)
    elif ProductCode == 'BDC':
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
        return add_dandao_main_material(listType)
    else:
        return "没有要新增的产品类型"