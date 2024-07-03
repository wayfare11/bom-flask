import pandas as pd

def calculate_level(id, subset, level, result, df):
    if not subset or subset[0] == "":
        result.append((id, level))
    else:
        result.append((id, level))
        for i, sub_id in enumerate(subset):
            calculate_level(sub_id, df.loc[df['material_id'] == sub_id, 'subset'].values[0], f"{level}.{i+1}", result, df)

def remove_decimal_suffix(value):
    str_value = str(value)
    if '.' in str_value:
        if str_value.endswith('.0'):
            return remove_decimal_suffix(int(value))
        else:
            return str_value
    else:
        return str(int(value))
    
def check_subset_and_show_message(df):
    for index, row in df.iterrows():
        if row['subset'][0] != "":
            items_to_remove = []
            for item in row['subset']:
                if item not in df['material_id'].values:
                    items_to_remove.append(item)
            df.at[index, 'subset'] = [x for x in row['subset'] if x not in items_to_remove]
    return df

def add_main_sort(df):
    # 确保 df 是原始 DataFrame 的副本，以避免 SettingWithCopyWarning
    df = df.copy()

    # 使用 .loc 方法进行赋值操作
    df.loc[:, 'subset'] = df.iloc[:, 12].apply(lambda x: x.split(','))
    df.loc[:, 'material_id'] = df.iloc[:, 14]

    df = check_subset_and_show_message(df)

    top_level_ids = set(df['material_id']) - set(sub_id for sublist in df['subset'] for sub_id in sublist)
    levels = []
    for i, id in enumerate(top_level_ids):
        calculate_level(id, df.loc[df['material_id'] == id, 'subset'].values[0], str(i+1), levels, df)
    level_df = pd.DataFrame(levels, columns=['material_id', 'level'])
    level_df['level'] = level_df['level'].apply(remove_decimal_suffix)

    # 使用 .loc 方法进行删除操作
    df.drop(['subset', 'material_id'], axis=1, inplace=True)

    selected_columns = list(df.columns[0:1]) + list(df.columns[14:])
    df = df[selected_columns]
    df.insert(0, 'serialNumber', '')
    df.columns = range(0, 14)
    df_temp = df.copy()

    rows_to_add = len(level_df) - len(df)
    empty_rows = pd.DataFrame([{} for _ in range(rows_to_add)])
    df = pd.concat([df, empty_rows], ignore_index=True)

    for i in range(len(level_df)):
        df.loc[i, 0] = level_df.loc[i, 'level']
        mask = df_temp.iloc[:, 2] == level_df.loc[i, 'material_id']
        if not df_temp[mask].empty:
            df.loc[i, 1:] = df_temp[mask].iloc[0, 1:]

    df = df.drop(df.columns[1], axis=1)
    df.columns = range(df.shape[1])
    return df

def divide_sort_data(data):
    # 将元组转换为 DataFrame
    df = pd.DataFrame(data)

    df_main = df[df.iloc[:, 13] == "主料"]
    df_packaging = df[df.iloc[:, 13] == "包材"]
    df_auxiliary = df[df.iloc[:, 13] == "辅材"]

    df_main = add_main_sort(df_main)
    df_packaging = add_main_sort(df_packaging)
    df_auxiliary = add_main_sort(df_auxiliary)

    df = pd.concat([df_main, df_packaging, df_auxiliary], ignore_index=True)

    # 将 DataFrame 转换回元组
    result = tuple(tuple(x) for x in df.values)
    return result
