class DandaoMainMaterialType:
    id = None
    MaterialCode = None
    fileCode = None
    Name = None
    ProductSpecifications = None
    Version = None
    ProductCode = None
    dandaoDiameter = None
    dandaoLength = None
    drainageMethod = None
    dandaoHeadStyle = None
    dandaoConfigurationCode = None

    def __init__(self, MaterialCode, fileCode, Name, ProductSpecifications, Version, ProductCode, dandaoDiameter, dandaoLength, drainageMethod, dandaoHeadStyle, dandaoConfigurationCode):
        self.MaterialCode = MaterialCode
        self.fileCode = fileCode
        self.Name = Name
        self.ProductSpecifications = ProductSpecifications
        self.Version = Version
        self.ProductCode = ProductCode
        self.dandaoDiameter = dandaoDiameter
        self.dandaoLength = dandaoLength
        self.drainageMethod = drainageMethod
        self.dandaoHeadStyle = dandaoHeadStyle
        self.dandaoConfigurationCode = dandaoConfigurationCode

class YinliuMainMaterialType:
    id = None
    MaterialCode = None
    fileCode = None
    Name = None
    ProductSpecifications = None
    Version = None
    ProductCode = None
    yinliuDiameter = None
    yinliuLength = None
    yinliuLockStyle = None
    yinliuHeadStyle = None
    yinliuConfigurationCode = None

    def __init__(self, MaterialCode, fileCode, Name, ProductSpecifications, Version, ProductCode, yinliuDiameter, yinliuLength, yinliuLockStyle, yinliuHeadStyle, yinliuConfigurationCode):
        self.MaterialCode = MaterialCode
        self.fileCode = fileCode
        self.Name = Name
        self.ProductSpecifications = ProductSpecifications
        self.Version = Version
        self.ProductCode = ProductCode
        self.yinliuDiameter = yinliuDiameter
        self.yinliuLength = yinliuLength
        self.yinliuLockStyle = yinliuLockStyle
        self.yinliuHeadStyle = yinliuHeadStyle
        self.yinliuConfigurationCode = yinliuConfigurationCode