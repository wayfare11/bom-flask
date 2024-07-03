from connectMysql.getConnect import get_database_connection
from componentMaterials.componentType import ComponentAddType


def addComponent(listType: ComponentAddType):
    try:
        con = get_database_connection()
        cursor = con.cursor()
        cursor.execute(
            f"insert into components values(null,'{listType.ProductCode}','{listType.dandaoDiameter}','{listType.dandaoLength}','{listType.drainageMethod}','{listType.dandaoHeadStyle}','{listType.dandaoConfigurationCode}','{listType.yinliuDiameter}','{listType.yinliuLength}','{listType.yinliuLockStyle}','{listType.yinliuHeadStyle}','{listType.yinliuConfigurationCode}','{listType.subset}','{listType.majorCategory}','{listType.materialCode}','{listType.drawingCode}','{listType.Name}','{listType.specification}','{listType.material}','{listType.color}','{listType.numbers}','{listType.unit}','{listType.materialCategory}','{listType.Note}','{listType.perPrice}',{listType.totalPrice})"
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


def addComponentList(data):
    # 从传递过来的数据中提取所需的值
    numbers = float(data["numbers"])
    perPrice = float(data["perPrice"])

    # 计算 totalPrice
    totalPrice = round(numbers * perPrice, 4)

    # 将 totalPrice 添加到数据中
    data["totalPrice"] = totalPrice

    # print("Data extracted from request:", data)

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

    if addComponent(listType) > 0:
        print("添加成功")
    else:
        print("添加失败")
