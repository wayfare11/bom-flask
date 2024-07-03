from connectMysql.getConnect import get_database_connection
from mainMaterials.specialNumEdit import edit_numbers
from mainMaterials.sortNumEdit import divide_sort_data

def list_dc_component(
    s_materialCode: str,
    s_name: str,
    s_majorCategory: str,
    s_productCode: str,
    s_yinliuDiameter: str,
    s_yinliuLength: str,
    s_yinliuLockStyle: str,
    s_yinliuHeadStyle: str,
    s_yinliuConfigurationCode: str,
):
    try:
        con = get_database_connection()
        cur = con.cursor()

        sql = "select * from components where 1=1"

        if s_materialCode.strip() != "":
            sql += " AND materialCode LIKE '%" + s_materialCode + "%'"
        if s_name.strip() != "":
            sql += " AND Name LIKE '%" + s_name + "%'"
        if s_majorCategory.strip() != "":
            sql += " AND majorCategory = '" + s_majorCategory + "'"
        if s_productCode:
            sql += " AND ProductCode REGEXP '(^|,)" + s_productCode + "($|,)'"
        if s_yinliuDiameter:
            sql += " AND yinliuDiameter REGEXP '(^|,)" + s_yinliuDiameter + "($|,)'"
        if s_yinliuLength:
            sql += " AND yinliuLength REGEXP '(^|,)" + s_yinliuLength + "($|,)'"
        if s_yinliuLockStyle:
            sql += " AND yinliuLockStyle REGEXP '(^|,)" + s_yinliuLockStyle + "($|,)'"
        if s_yinliuHeadStyle:
            sql += " AND yinliuHeadStyle REGEXP '(^|,)" + s_yinliuHeadStyle + "($|,)'"
        if s_yinliuConfigurationCode:
            sql += (
                " AND yinliuConfigurationCode REGEXP '(^|,)"
                + s_yinliuConfigurationCode
                + "($|,)'"
            )

        cur.execute(sql)
        return cur.fetchall()
    except Exception as e:
        print(e)
        return None
    finally:
        cur.close()
        con.close()


def list_bdc_component(
    s_materialCode: str,
    s_name: str,
    s_majorCategory: str,
    s_productCode: str,
    s_dandaoDiameter: str,
    s_dandaoLength: str,
    s_drainageMethod: str,
    s_dandaoHeadStyle: str,
    s_dandaoConfigurationCode: str,
):
    try:
        con = get_database_connection()
        cur = con.cursor()

        sql = "select * from components where 1=1"

        if s_materialCode.strip() != "":
            sql += " AND materialCode LIKE '%" + s_materialCode + "%'"
        if s_name.strip() != "":
            sql += " AND Name LIKE '%" + s_name + "%'"
        if s_majorCategory.strip() != "":
            sql += " AND majorCategory = '" + s_majorCategory + "'"
        if s_productCode:
            sql += " AND ProductCode REGEXP '(^|,)" + s_productCode + "($|,)'"
        if s_dandaoDiameter:
            sql += " AND dandaoDiameter REGEXP '(^|,)" + s_dandaoDiameter + "($|,)'"
        if s_dandaoLength:
            sql += " AND dandaoLength REGEXP '(^|,)" + s_dandaoLength + "($|,)'"
        if s_drainageMethod:
            sql += " AND drainageMethod REGEXP '(^|,)" + s_drainageMethod + "($|,)'"
        if s_dandaoHeadStyle:
            sql += " AND dandaoHeadStyle REGEXP '(^|,)" + s_dandaoHeadStyle + "($|,)'"
        if s_dandaoConfigurationCode:
            sql += (
                " AND dandaoConfigurationCode REGEXP '(^|,)"
                + s_dandaoConfigurationCode
                + "($|,)'"
            )

        cur.execute(sql)
        return cur.fetchall()
    except Exception as e:
        print(e)
        return None
    finally:
        cur.close()
        con.close()


def check_main_materials(data):
    materialCode = data.get("materialCode", "")
    Name = data.get("Name", "")
    majorCategory = data.get("majorCategory", "")
    productCode = data.get("productCode", "")

    json_data = []

    if productCode == "DC":
        yinliuDiameter = data.get("yinliuDiameter", "")
        yinliuLength = data.get("yinliuLength", "")
        yinliuLockStyle = data.get("yinliuLockStyle", "")
        yinliuHeadStyle = data.get("yinliuHeadStyle", "")
        yinliuConfigurationCode = data.get("yinliuConfigurationCode", "")
        data_fetch = list_dc_component(
            materialCode,
            Name,
            majorCategory,
            productCode,
            yinliuDiameter,
            yinliuLength,
            yinliuLockStyle,
            yinliuHeadStyle,
            yinliuConfigurationCode,
        )
        data_fetch = edit_numbers(data_fetch, yinliuHeadStyle, yinliuDiameter, yinliuLength, yinliuConfigurationCode)
        data_fetch = divide_sort_data(data_fetch)
    elif productCode == "BDC":
        dandaoDiameter = data.get("dandaoDiameter", "")
        dandaoLength = data.get("dandaoLength", "")
        drainageMethod = data.get("drainageMethod", "")
        dandaoHeadStyle = data.get("dandaoHeadStyle", "")
        dandaoConfigurationCode = data.get("dandaoConfigurationCode", "")
        data_fetch = list_bdc_component(
            materialCode,
            Name,
            majorCategory,
            productCode,
            dandaoDiameter,
            dandaoLength,
            drainageMethod,
            dandaoHeadStyle,
            dandaoConfigurationCode,
        )
        data_fetch = edit_numbers(data_fetch, drainageMethod, dandaoDiameter, dandaoLength, dandaoConfigurationCode)
        data_fetch = divide_sort_data(data_fetch)
    else:
        data_fetch = []
    
    for item in data_fetch:
        numbers = float(item[7])
        perPrice = float(item[11])
        totalPrice = round(numbers * perPrice, 4)
        json_data.append({
            "index": item[0],
            "materialCode": item[1],
            "drawingCode": item[2],
            "Name": item[3],
            "specification": item[4],
            "material": item[5],
            "color": item[6],
            "numbers": numbers,
            "unit": item[8],
            "materialCategory": item[9],
            "Note": item[10],
            "perPrice": perPrice,
            "totalPrice": totalPrice
        })
    return json_data
