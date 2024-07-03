class ComponentUpdateConditionType:
    ProductCode = None
    dandaoDiameter = None
    dandaoLength = None
    drainageMethod = None
    dandaoHeadStyle = None
    dandaoConfigurationCode = None
    yinliuDiameter = None
    yinliuLength = None
    yinliuLockStyle = None
    yinliuHeadStyle = None
    yinliuConfigurationCode = None

    def __init__(
        self,
        ProductCode,
        dandaoDiameter,
        dandaoLength,
        drainageMethod,
        dandaoHeadStyle,
        dandaoConfigurationCode,
        yinliuDiameter,
        yinliuLength,
        yinliuLockStyle,
        yinliuHeadStyle,
        yinliuConfigurationCode,
    ):
        self.ProductCode = ProductCode
        self.dandaoDiameter = dandaoDiameter
        self.dandaoLength = dandaoLength
        self.drainageMethod = drainageMethod
        self.dandaoHeadStyle = dandaoHeadStyle
        self.dandaoConfigurationCode = dandaoConfigurationCode
        self.yinliuDiameter = yinliuDiameter
        self.yinliuLength = yinliuLength
        self.yinliuLockStyle = yinliuLockStyle
        self.yinliuHeadStyle = yinliuHeadStyle
        self.yinliuConfigurationCode = yinliuConfigurationCode


class ComponentAddType:
    ProductCode = ""
    dandaoDiameter = ""
    dandaoLength = ""
    drainageMethod = ""
    dandaoHeadStyle = ""
    dandaoConfigurationCode = ""
    yinliuDiameter = ""
    yinliuLength = ""
    yinliuLockStyle = ""
    yinliuHeadStyle = ""
    yinliuConfigurationCode = ""
    subset = ""

    majorCategory = None
    materialCode = None
    drawingCode = None
    Name = None
    specification = None
    material = None
    color = None
    numbers = None
    unit = None
    materialCategory = None
    Note = None
    perPrice = None
    totalPrice = None

    def __init__(
        self,
        majorCategory,
        materialCode,
        drawingCode,
        Name,
        specification,
        material,
        color,
        numbers,
        unit,
        materialCategory,
        Note,
        perPrice,
        totalPrice,
    ):
        self.majorCategory = majorCategory
        self.materialCode = materialCode
        self.drawingCode = drawingCode
        self.Name = Name
        self.specification = specification
        self.material = material
        self.color = color
        self.numbers = numbers
        self.unit = unit
        self.materialCategory = materialCategory
        self.Note = Note
        self.perPrice = perPrice
        self.totalPrice = totalPrice
