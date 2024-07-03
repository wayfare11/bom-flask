def edit_numbers(data, s_headStyle, s_diameter, s_length, s_configCode):
    # 将数据转换为列表，以便修改
    data = [list(row) for row in data]

    # 添加48410022物料的用量设计
    for row in data:
        if row[14] == "48410022":
            if s_configCode == "T":
                row[20] = "0.02"
                row[21] = "张"
            else:
                row[20] = "0.1"
                row[21] = "张"

    # 添加99410001物料的用量设计
    for row in data:
        if row[14] == "99410001":
            if s_configCode == "T":
                row[20] = "1.22"
                row[21] = "个"
            else:
                row[20] = "1.3"
                row[21] = "个"

    # 添加48410023物料的用量设计
    for row in data:
        if row[14] == "48410023":
            if s_configCode == "T":
                row[20] = "0.02"
                row[21] = "张"
            else:
                row[20] = "0.1"
                row[21] = "张"

    # 添加49200170物料的用量设计
    for row in data:
        if row[14] == "49200170":
            if s_configCode == "T":
                row[20] = "0.02"
                row[21] = "张"
            else:
                row[20] = "0.1"
                row[21] = "张"

    # 软套管管材为0.33用量的判断条件
    judge_rt_033_1 = (s_headStyle == "None") and (s_diameter in ["08", "10", "12"]) and (s_length == "35")
    judge_rt_033_2 = (s_headStyle in ["W", "P", "J"]) and (s_diameter in ["08", "10", "12", "14", "16"]) and (s_length == "40")
    judge_rt_033_3 = (s_headStyle == "W") and (s_diameter == "07") and (s_length == "25")
    
    # 软套管管材为0.2用量的判断条件
    judge_rt_020_1 = (s_headStyle in ["P", "J"]) and (s_diameter in ["08", "10", "12", "14", "16"]) and (s_length == "20")
    judge_rt_020_2 = (s_headStyle in ["W", "P", "J"]) and (s_diameter in ["08", "10", "12", "14", "16"]) and (s_length == "25")

    # 软套管管材为0.25用量的判断条件
    judge_rt_025_1 = (s_headStyle in ["W", "P", "J"]) and (s_diameter in ["08", "10", "12", "14", "16"]) and (s_length == "30")
    judge_rt_025_2 = (s_headStyle in ["W", "P", "J"]) and (s_diameter in ["08", "10", "12", "14", "16"]) and (s_length == "35")

    # 软套管管材为0.5用量的判断条件
    judge_rt_050_1 = (s_headStyle == "W") and (s_diameter == "07") and (s_length == "30")
    judge_rt_050_2 = (s_headStyle == "W") and (s_diameter == "07") and (s_length == "35")
    judge_rt_050_3 = (s_headStyle == "W") and (s_diameter == "07") and (s_length == "40")

    # 判断是否有软套管管材
    for row in data:
        if "软套管管材" in row[16]:
            if judge_rt_033_1 or judge_rt_033_2 or judge_rt_033_3:
                row[20] = "0.33"
                row[21] = "根"
            elif judge_rt_020_1 or judge_rt_020_2:
                row[20] = "0.2"
                row[21] = "根"
            elif judge_rt_025_1 or judge_rt_025_2:
                row[20] = "0.25"
                row[21] = "根"
            elif judge_rt_050_1 or judge_rt_050_2 or judge_rt_050_3:
                row[20] = "0.5"
                row[21] = "根"
            else:
                row[20] = "/"
                row[21] = "根"

    # 固定拉线长度为1.3
    judge_gd_13_1 = (s_headStyle == "None") and (s_diameter in ["08", "10", "12"]) and (s_length == "35")
    judge_gd_13_2 = (s_headStyle in ["W", "P", "J"]) and (s_diameter in ["08", "10", "12", "14", "16"]) and (s_length == "35")
    judge_gd_13_3 = (s_headStyle == "W") and (s_diameter == "07") and (s_length == "35")
    judge_gd_13_4 = (s_headStyle in ["W", "P", "J"]) and (s_diameter in ["05", "06"]) and (s_length == "35")

    # 固定拉线长度为1.0
    judge_gd_10_1 = (s_headStyle in ["P", "J"]) and (s_diameter in ["05", "06", "08", "10", "12", "14", "16"]) and (s_length == "20")

    # 固定拉线长度为1.1
    judge_gd_11_1 = (s_headStyle in ["W", "P", "J"]) and (s_diameter in ["08", "10", "12", "14", "16"]) and (s_length == "25")
    judge_gd_11_2 = (s_headStyle == "W") and (s_diameter == "07") and (s_length == "25")
    judge_gd_11_3 = (s_headStyle in ["W", "P", "J"]) and (s_diameter in ["05", "06"]) and (s_length == "25")

    # 固定拉线长度为1.2
    judge_gd_12_1 = (s_headStyle in ["W", "P", "J"]) and (s_diameter in ["08", "10", "12", "14", "16"]) and (s_length == "30")
    judge_gd_12_2 = (s_headStyle == "W") and (s_diameter == "07") and (s_length == "30")
    judge_gd_12_3 = (s_headStyle in ["W", "P", "J"]) and (s_diameter in ["05", "06"]) and (s_length == "30")

    # 固定拉线长度为1.4
    judge_gd_14_1 = (s_headStyle in ["W", "P", "J"]) and (s_diameter in ["08", "10", "12", "14", "16"]) and (s_length == "40")
    judge_gd_14_2 = (s_headStyle == "W") and (s_diameter == "07") and (s_length == "40")
    judge_gd_14_3 = (s_headStyle in ["W", "P", "J"]) and (s_diameter in ["05", "06"]) and (s_length == "40")

    # 判断是否有固定拉线
    for row in data:
        if "固定拉线" in row[16]:
            if judge_gd_13_1 or judge_gd_13_2 or judge_gd_13_3 or judge_gd_13_4:
                row[20] = "1.3"
                row[21] = "米"
            elif judge_gd_10_1:
                row[20] = "1.0"
                row[21] = "米"
            elif judge_gd_11_1 or judge_gd_11_2 or judge_gd_11_3:
                row[20] = "1.1"
                row[21] = "米"
            elif judge_gd_12_1 or judge_gd_12_2 or judge_gd_12_3:
                row[20] = "1.2"
                row[21] = "米"
            elif judge_gd_14_1 or judge_gd_14_2 or judge_gd_14_3:
                row[20] = "1.4"
                row[21] = "米"

    # 将数据转换回元组
    data = tuple(tuple(row) for row in data)
    return data
