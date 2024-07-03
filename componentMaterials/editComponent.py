from connectMysql.getConnect import get_database_connection
from componentMaterials.componentType import ComponentAddType

def editComponent(listType: ComponentAddType, id):
    try:
        con = get_database_connection()
        cursor = con.cursor()
        sql = "update components set majorCategory=%s,materialCode=%s,drawingCode=%s,Name=%s,specification=%s,material=%s,color=%s,numbers=%s,unit=%s,materialCategory=%s,Note=%s,perPrice=%s,totalPrice=%s"
        sql += " where id = %s"

        cursor.execute(
            sql,
            (
                listType.majorCategory,
                listType.materialCode,
                listType.drawingCode,
                listType.Name,
                listType.specification,
                listType.material,
                listType.color,
                listType.numbers,
                listType.unit,
                listType.materialCategory,
                listType.Note,
                listType.perPrice,
                listType.totalPrice,
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


def edit_component_from_database(data):
    
    numbers = float(data["numbers"])
    perPrice = float(data["perPrice"])

    # 计算 totalPrice
    totalPrice = round(numbers * perPrice, 4)

    # 将 totalPrice 添加到数据中
    data["totalPrice"] = totalPrice

    # print("Data extracted from request:", data)
    id = data["id"]

    listType = ComponentAddType(
        majorCategory=data["majorCategory"],
        materialCode=data["materialCode"],
        drawingCode=data["drawingCode"],
        Name=data["Name"],
        specification=data["specification"],
        material=data["material"],
        color=data["color"],
        numbers=data["numbers"],
        unit=data["unit"],
        materialCategory=data["materialCategory"],
        Note=data["Note"],
        perPrice=data["perPrice"],
        totalPrice=data["totalPrice"],
    )

    if editComponent(listType, id) > 0:
        print("修改成功")
    else:
        print("修改失败")
