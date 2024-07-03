import pandas as pd
import math
from mainMaterials.checkMainMaterials import check_main_materials
from mainMaterials.setExcel import setExcel, setAppendixExcel
from flask_socketio import emit


def download_excel(data_name, socketio):

    excel_file_name = f"./saveExcel/{data_name['customFileName']}.xlsx"
    data = data_name['selectedRows']
    total_steps = len(data)

    try:
        with pd.ExcelWriter(excel_file_name) as writer:
            Appendix_data = [
                ["附录：", "", "", ""],
                ["序号", "产品规格", "物料编码", "文件编号"],
            ]
            pd.DataFrame(Appendix_data).to_excel(
                writer, sheet_name="附录", index=False, header=False
            )

            for idx in range(len(data)):
                download_name = (
                    str(idx + 1)
                    + "-"
                    + data[idx]["ProductSpecifications"].replace("/", " ")
                )

                Appendix_data.append(
                    [
                        str(idx + 1),
                        data[idx]["ProductSpecifications"],
                        data[idx]["MaterialCode"],
                        data[idx]["fileCode"],
                    ]
                )

                file_name = "文件编号：" + data[idx]["fileCode"]
                version = "版本号：" + data[idx]["Version"]
                product_style = "产品规格：" + data[idx]["ProductSpecifications"]
                material_code = "物料编码：" + data[idx]["MaterialCode"]

                temp_data = pd.DataFrame("", index=range(3), columns=range(11))

                temp_data.iloc[0, 0] = data[idx]["Name"]
                temp_data.iloc[1, 0] = file_name
                temp_data.iloc[1, 5] = version
                temp_data.iloc[2, 0] = product_style
                temp_data.iloc[2, 5] = material_code

                # 添加零部件的列名
                column_names = pd.DataFrame(
                    [
                        "序号",
                        "物料编码",
                        "图纸号",
                        "名称",
                        "规格/型号",
                        "材料",
                        "颜色",
                        "数量",
                        "单位",
                        "物料类别",
                        "备注",
                    ]
                ).T

                temp_data = pd.concat(
                    [temp_data, column_names], axis=0, ignore_index=True
                )

                # 添加零部件数据, 设置查询条件
                productCode = data[idx]["ProductCode"]
                if productCode == "DC":
                    input_data_main = {
                        "materialCode": "",
                        "Name": "",
                        "majorCategory": "主料",
                        "productCode": productCode,
                        "yinliuDiameter": data[idx]["yinliuDiameter"],
                        "yinliuLength": data[idx]["yinliuLength"],
                        "yinliuLockStyle": data[idx]["yinliuLockStyle"],
                        "yinliuHeadStyle": data[idx]["yinliuHeadStyle"],
                        "yinliuConfigurationCode": data[idx]["yinliuConfigurationCode"],
                    }
                    input_data_packaging = {
                        "materialCode": "",
                        "Name": "",
                        "majorCategory": "包材",
                        "productCode": productCode,
                        "yinliuDiameter": data[idx]["yinliuDiameter"],
                        "yinliuLength": data[idx]["yinliuLength"],
                        "yinliuLockStyle": data[idx]["yinliuLockStyle"],
                        "yinliuHeadStyle": data[idx]["yinliuHeadStyle"],
                        "yinliuConfigurationCode": data[idx]["yinliuConfigurationCode"],
                    }
                    input_data_auxiliary = {
                        "materialCode": "",
                        "Name": "",
                        "majorCategory": "辅材",
                        "productCode": productCode,
                        "yinliuDiameter": data[idx]["yinliuDiameter"],
                        "yinliuLength": data[idx]["yinliuLength"],
                        "yinliuLockStyle": data[idx]["yinliuLockStyle"],
                        "yinliuHeadStyle": data[idx]["yinliuHeadStyle"],
                        "yinliuConfigurationCode": data[idx]["yinliuConfigurationCode"],
                    }
                    data_components_main = pd.DataFrame(
                        check_main_materials(input_data_main)
                    ).iloc[:, :11]
                    data_components_packaging = pd.DataFrame(
                        check_main_materials(input_data_packaging)
                    ).iloc[:, :11]
                    data_components_auxiliary = pd.DataFrame(
                        check_main_materials(input_data_auxiliary)
                    ).iloc[:, :11]

                    data_components_main.columns = range(11)
                    data_components_packaging.columns = range(11)
                    data_components_auxiliary.columns = range(11)
                elif productCode == "BDC":
                    input_data_main = {
                        "materialCode": "",
                        "Name": "",
                        "majorCategory": "主料",
                        "productCode": productCode,
                        "dandaoDiameter": data[idx]["dandaoDiameter"],
                        "dandaoLength": data[idx]["dandaoLength"],
                        "drainageMethod": data[idx]["drainageMethod"],
                        "dandaoHeadStyle": data[idx]["dandaoHeadStyle"],
                        "dandaoConfigurationCode": data[idx]["dandaoConfigurationCode"],
                    }
                    input_data_packaging = {
                        "materialCode": "",
                        "Name": "",
                        "majorCategory": "包材",
                        "productCode": productCode,
                        "dandaoDiameter": data[idx]["dandaoDiameter"],
                        "dandaoLength": data[idx]["dandaoLength"],
                        "drainageMethod": data[idx]["drainageMethod"],
                        "dandaoHeadStyle": data[idx]["dandaoHeadStyle"],
                        "dandaoConfigurationCode": data[idx]["dandaoConfigurationCode"],
                    }
                    input_data_auxiliary = {
                        "materialCode": "",
                        "Name": "",
                        "majorCategory": "辅材",
                        "productCode": productCode,
                        "dandaoDiameter": data[idx]["dandaoDiameter"],
                        "dandaoLength": data[idx]["dandaoLength"],
                        "drainageMethod": data[idx]["drainageMethod"],
                        "dandaoHeadStyle": data[idx]["dandaoHeadStyle"],
                        "dandaoConfigurationCode": data[idx]["dandaoConfigurationCode"],
                    }
                    data_components_main = pd.DataFrame(
                        check_main_materials(input_data_main)
                    ).iloc[:, :11]
                    data_components_packaging = pd.DataFrame(
                        check_main_materials(input_data_packaging)
                    ).iloc[:, :11]
                    data_components_auxiliary = pd.DataFrame(
                        check_main_materials(input_data_auxiliary)
                    ).iloc[:, :11]

                    data_components_main.columns = range(11)
                    data_components_packaging.columns = range(11)
                    data_components_auxiliary.columns = range(11)
                else:
                    data_components_main = []
                    data_components_packaging = []
                    data_components_auxiliary = []

                temp_data = pd.concat(
                    [temp_data, data_components_main], axis=0, ignore_index=True
                )

                index_packaging = len(temp_data) + 1  # 添加标题序号
                empty_row = pd.DataFrame([[""] * 11], columns=range(11))  # 创建空行数据
                # 空行数据设为标题名
                data_components_packaging = pd.concat(
                    [empty_row, data_components_packaging], ignore_index=True
                )
                data_components_packaging.iloc[0, 0] = "包材"

                temp_data = pd.concat(
                    [temp_data, data_components_packaging], axis=0, ignore_index=True
                )

                index_auxiliary = len(temp_data) + 1
                data_components_auxiliary = pd.concat(
                    [empty_row, data_components_auxiliary], ignore_index=True
                )
                data_components_auxiliary.iloc[0, 0] = "辅材"

                temp_data = pd.concat(
                    [temp_data, data_components_auxiliary], axis=0, ignore_index=True
                )

                # 将数据写入不同的 sheet 页
                temp_data.to_excel(
                    writer, sheet_name=download_name, index=False, header=False
                )

                # 获取当前 sheet
                sheet = writer.sheets[download_name]

                setExcel(sheet, index_packaging, index_auxiliary)

                socketio.emit('progress', {'progress': math.floor(idx/total_steps * 100)})

            # 循环结束后，将Appendix_data转换为DataFrame
            appendix_df = pd.DataFrame(Appendix_data)
            # 将DataFrame写入到Excel文件的第一个sheet中，并将该sheet命名为"附录"
            appendix_df.to_excel(writer, sheet_name="附录", index=False, header=False)
            sheet = writer.sheets["附录"]
            setAppendixExcel(sheet)

    except Exception as e:
        print(e)
        socketio.emit('progress', {'progress': 100, 'error': str(e)})
        return "failed"

    return "success"
