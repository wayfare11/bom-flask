import os
from flask import Flask, request, send_file
from flask_cors import CORS

from roleManage.user_auth import login
from roleManage.judgeRole import judgeRole
from roleManage.getRoleList import getRoleList
from roleManage.addRole import add_role
from roleManage.editRole import edit_role
from roleManage.deleteRole import delete_role
from roleManage.judgeUserNameExist import judge_user_name_exist

from flask_socketio import SocketIO, emit

from mainMaterials.allMaterialList import get_all_list_data
from mainMaterials.dcMaterialList import get_dc_list_data
from mainMaterials.bdcMaterialList import get_bdc_list_data
from mainMaterials.addFinishedMaterials import add_main_material
from mainMaterials.deleteFinishedMaterials import delete_finished_materials
from mainMaterials.editFinishedMaterials import edit_finished_materials
from mainMaterials.checkMainMaterials import check_main_materials
from mainMaterials.download import download_excel

from componentMaterials.allComponentList import get_all_component_list_data
from componentMaterials.addComponent import addComponentList
from componentMaterials.deleteComponent import delete_component_from_database
from componentMaterials.editComponent import edit_component_from_database
from componentMaterials.conditionSet import condition_set_from_database
from componentMaterials.idExcept import get_id_except_from_database
from componentMaterials.sonSet import sonSet
from componentMaterials.judgeSonSet import judge_son_set_exist

from roleManage.logsManage import add_logs, get_logs_list

app = Flask(__name__)

CORS(app)

socketio = SocketIO(app, cors_allowed_origins="*")

# 路由来处理用户验证
@app.route('/login', methods=['POST'])
def login_route():
    return login()

@app.route('/allList', methods=['GET'])
def all_list():
    return get_all_list_data()

@app.route('/dcList', methods=['GET'])
def dc_list():
    yinliuDiameter = request.args.get('yinliuDiameter', '')
    yinliuLength = request.args.get('yinliuLength', '')
    yinliuLockStyle = request.args.get('yinliuLockStyle', '')
    yinliuHeadStyle = request.args.get('yinliuHeadStyle', '')
    yinliuConfigurationCode = request.args.get('yinliuConfigurationCode', '')
    return get_dc_list_data(yinliuDiameter, yinliuLength, yinliuLockStyle, yinliuHeadStyle, yinliuConfigurationCode)

@app.route('/bdcList', methods=['GET'])
def bdc_list():
    dandaoDiameter = request.args.get('dandaoDiameter', '')
    dandaoLength = request.args.get('dandaoLength', '')
    drainageMethod = request.args.get('drainageMethod', '')
    dandaoHeadStyle = request.args.get('dandaoHeadStyle', '')
    dandaoConfigurationCode = request.args.get('dandaoConfigurationCode', '')

    return get_bdc_list_data(dandaoDiameter, dandaoLength, drainageMethod, dandaoHeadStyle, dandaoConfigurationCode)

@app.route('/componentList', methods=['GET'])
def component_list():
    componentName = request.args.get('componentName', '')
    componentMaterialCode = request.args.get('componentMaterialCode', '')
    return get_all_component_list_data(componentName, componentMaterialCode)

@app.route('/addComponent', methods=['POST'])
def add_component():
    data = request.json
    majorCategory = data.get('majorCategory', '')
    materialCode = data.get('materialCode', '')
    drawingCode = data.get('drawingCode', '')
    Name = data.get('Name', '')
    specification = data.get('specification', '')
    material = data.get('material', '')
    color = data.get('color', '')
    numbers = data.get('numbers', '')
    unit = data.get('unit', '')
    materialCategory = data.get('materialCategory', '')
    Note = data.get('Note', '')
    perPrice = data.get('perPrice', '')
    
    data = {
        'majorCategory': majorCategory,
        'materialCode': materialCode,
        'drawingCode': drawingCode,
        'Name': Name,
        'specification': specification,
        'material': material,
        'color': color,
        'numbers': numbers,
        'unit': unit,
        'materialCategory': materialCategory,
        'Note': Note,
        'perPrice': perPrice
    }
    
    addComponentList(data)  # 将数据传递给 addComponentList 函数
    return "Component added successfully"

@app.route('/deleteComponent', methods=['DELETE'])
def delete_component():
    # 前端传过来的是一个 id 的数组
    id_array = request.args.getlist('id')  # 获取传递过来的ID数组

    success_count = 0
    for component_id in id_array:
        # 执行删除操作，例如从数据库中删除对应的记录
        if delete_component_from_database(component_id):
            success_count += 1

    if success_count == len(id_array):
        return '删除成功'
    else:
        return '删除失败'
    
@app.route('/editComponent', methods=['PUT'])
def edit_component():
    data = request.json
    id = data.get('id', '')
    majorCategory = data.get('majorCategory', '')
    materialCode = data.get('materialCode', '')
    drawingCode = data.get('drawingCode', '')
    Name = data.get('Name', '')
    specification = data.get('specification', '')
    material = data.get('material', '')
    color = data.get('color', '')
    numbers = data.get('numbers', '')
    unit = data.get('unit', '')
    materialCategory = data.get('materialCategory', '')
    Note = data.get('Note', '')
    perPrice = data.get('perPrice', '')

    data = {
        'id': id,
        'majorCategory': majorCategory,
        'materialCode': materialCode,
        'drawingCode': drawingCode,
        'Name': Name,
        'specification': specification,
        'material': material,
        'color': color,
        'numbers': numbers,
        'unit': unit,
        'materialCategory': materialCategory,
        'Note': Note,
        'perPrice': perPrice
    }

    edit_component_from_database(data)  # 将数据传递给 edit_component_from_database 函数
    return "edit component"

@app.route('/conditionSet', methods=['PUT'])
def condition_set():
    data = request.json
    id = data.get('id', '')
    ProductCode = data.get('ProductCode', '')
    yinliuDiameter = data.get('yinliuDiameter', '')
    yinliuLength = data.get('yinliuLength', '')
    yinliuLockStyle = data.get('yinliuLockStyle', '')
    yinliuHeadStyle = data.get('yinliuHeadStyle', '')
    yinliuConfigurationCode = data.get('yinliuConfigurationCode', '')
    dandaoDiameter = data.get('dandaoDiameter', '')
    dandaoLength = data.get('dandaoLength', '')
    drainageMethod = data.get('drainageMethod', '')
    dandaoHeadStyle = data.get('dandaoHeadStyle', '')
    dandaoConfigurationCode = data.get('dandaoConfigurationCode', '')

    data = {
        'id': id,
        'ProductCode': ProductCode,
        'yinliuDiameter': yinliuDiameter,
        'yinliuLength': yinliuLength,
        'yinliuLockStyle': yinliuLockStyle,
        'yinliuHeadStyle': yinliuHeadStyle,
        'yinliuConfigurationCode': yinliuConfigurationCode,
        'dandaoDiameter': dandaoDiameter,
        'dandaoLength': dandaoLength,
        'drainageMethod': drainageMethod,
        'dandaoHeadStyle': dandaoHeadStyle,
        'dandaoConfigurationCode': dandaoConfigurationCode
    }

    condition_set_from_database(data)  # 将数据传递给 conditionSet 函数

    return "condition set"

@app.route('/idExceptList', methods=['GET'])
def id_except_list():
    id = request.args.get('id', '')  # 从查询字符串中获取id参数
    materialCode = request.args.get('materialCode', '')  # 从查询字符串中获取materialCode参数
    Name = request.args.get('Name', '')  # 从查询字符串中获取name参数

    data = {
        'id': id,
        'materialCode': materialCode,
        'Name': Name
    }

    return get_id_except_from_database(data)

@app.route('/sonSet', methods=['PUT'])
def put_son_set():
    id = request.args.get('id', '')  # 从查询字符串中获取id参数
    son_set = request.args.get('son_set', '')  # 从查询字符串中获取son_set参数

    # print('id',id)
    # print('son_set',son_set)

    if sonSet(id, son_set) > 0:  # 将数据传递给 sonSet 函数
        return "修改子级成功"
    else:
        return "修改子级失败"

@app.route('/addMainMaterial', methods=['POST'])
def add_main_materials():
    data = request.json
    if add_main_material(data) > 0:
        return "添加主材料成功"
    else:
        return "添加主材料失败"
    
@app.route('/deleteFinishedMaterials', methods=['DELETE'])
def delete_finished_materials_route():
    id_array = request.args.getlist('id')  # 获取传递过来的ID数组
    productCode_array = request.args.getlist('productCode')  # 获取传递过来的productCode数组
    # 添加日志记录
    print("Received ID array:", id_array)
    print("Received ProductCode array:", productCode_array)
    success_count = 0
    for i in range(len(id_array)):
        print(productCode_array[i], id_array[i])
        if delete_finished_materials(productCode_array[i], id_array[i]):
            success_count += 1
    if success_count == len(id_array):
        return '删除成功'
    else:
        return '删除失败'
    
@app.route('/editFinishedMaterials', methods=['PUT'])
def edit_finished_materials_route():
    data = request.json
    if edit_finished_materials(data) > 0:
        return "修改成品成功"
    else:
        return "修改成品失败"

@app.route('/checkMainMaterial', methods=['GET'])
def check_main_material():
    data = request.args.to_dict()
    return check_main_materials(data)

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    return download_excel(data, socketio)

@app.route('/downloadFile', methods=['GET'])
def download_file():
    filename = request.args.get('filename')
    if not filename:
        return "文件名未提供", 400
    
    file_path = './saveExcel/' + filename + '.xlsx'
    print('file_path', file_path)
    if os.path.exists(file_path):
        socketio.emit('progress', {'progress': 100})
        return send_file(file_path, as_attachment=True)
    else:
        return "文件不存在", 404

@app.route('/judgeSonSet', methods=['GET'])
def judge_son_set():
    judge_method = request.args.get('judge_method', '')  # 从查询字符串中获取judge_method参数
    parent_materialCode = request.args.get('parent_materialCode', '')  # 从查询字符串中获取current_materialCode参数
    sonSets_materialCode = request.args.get('sonSets_materialCode', '')  # 从查询字符串中获取current_materialCode参数

    print('parent_materialCode', parent_materialCode)
    print('sonSets_materialCode', sonSets_materialCode)

    if judge_method == 'judge_son':
        for sonSet_materialCode in sonSets_materialCode.split(','):
            if judge_son_set_exist(parent_materialCode, sonSet_materialCode):
                return f"{sonSet_materialCode}内已存在子级{parent_materialCode}"
            else:
                continue
        return "success"
    
    elif judge_method == "judge_parent":
        if judge_son_set_exist(parent_materialCode, sonSets_materialCode):
            return f"{parent_materialCode}内已存在父级{sonSets_materialCode}"
        else:
            return "success"

@app.route('/roleList', methods=['GET'])
def role_list():
    userName = request.args.get('userName', '')  # 从查询字符串中获取username参数
    superRoot = request.args.get('superRoot', '')  # 从查询字符串中获取superRoot参数
    return getRoleList(userName, superRoot)

@app.route('/judgeRole', methods=['GET'])
def judge_role():
    role_id = request.args.get('role_id', '')  # 从查询字符串中获取role_id参数
    permission_operation = request.args.get('permission_operation', '')  # 从查询字符串中获取permission_operation参数
    return judgeRole(role_id, permission_operation)

@app.route('/judgeUserName', methods=['GET'])
def judge_user_name():
    username = request.args.get('username', '')  # 从查询字符串中获取username参数
    if judge_user_name_exist(username) > 0:
        return "True"
    else:
        return "False"

@app.route('/roleAdd', methods=['POST'])
def role_add():
    data = request.json
    username = data.get('username', '')
    password = data.get('password', '')
    super_root = data.get('super_root', 0)
    normal_root = data.get('normal_root', 0)
    add_data_permission = data.get('add_data_permission', 0)
    edit_data_permission = data.get('edit_data_permission', 0)
    delete_data_permission = data.get('delete_data_permission', 0)

    role_data = {
        'username': username,
        'password': password,
        'super_root': super_root,
        'normal_root': normal_root,
        'add_data_permission': add_data_permission,
        'edit_data_permission': edit_data_permission,
        'delete_data_permission': delete_data_permission
    }

    if add_role(role_data) > 0:
        return "添加角色成功"
    else:
        return "添加角色失败"
    
@app.route('/roleEdit', methods=['PUT'])
def role_edit():
    data = request.json
    role_id = data.get('role_id', '')
    username = data.get('username', '')
    password = data.get('password', '')
    super_root = data.get('super_root', 0)
    normal_root = data.get('normal_root', 0)
    add_data_permission = data.get('add_data_permission', 0)
    edit_data_permission = data.get('edit_data_permission', 0)
    delete_data_permission = data.get('delete_data_permission', 0)

    role_data = {
        'role_id': role_id,
        'username': username,
        'password': password,
        'super_root': super_root,
        'normal_root': normal_root,
        'add_data_permission': add_data_permission,
        'edit_data_permission': edit_data_permission,
        'delete_data_permission': delete_data_permission
    }

    if edit_role(role_data) > 0:
        return "修改角色成功"
    else:
        return "修改角色失败"
    
@app.route('/roleDelete', methods=['DELETE'])
def role_delete():
    role_id = request.args.getlist('role_id')  # 从查询字符串中获取role_id参数
    print(role_id)

    success_count = 0
    for role in role_id:
        if delete_role(role) > 0:
            success_count += 1
    if success_count == len(role_id):
        return "删除角色成功"
    else:
        return "删除角色失败"

@app.route('/logsAdd', methods=['POST'])
def logs_add():
    data = request.json
    user_name = data.get('user_name', '')
    user_identity = data.get('user_identity', '')
    operation_type = data.get('operation_type', '')
    operation_content = data.get('operation_content', '')
    operation_time = data.get('operation_time', '')

    logs_data = {
        'user_name': user_name,
        'user_identity': user_identity,
        'operation_type': operation_type,
        'operation_content': operation_content,
        'operation_time': operation_time
    }
    if add_logs(logs_data) > 0:
        return "添加日志成功"
    else:
        return "添加日志失败"

@app.route('/logsList', methods=['GET'])
def logs_list():
    user_name = request.args.get('user_name', '')  # 从查询字符串中获取user_name参数
    user_identity = request.args.get('user_identity', '')  # 从查询字符串中获取user_identity参数
    operation_type = request.args.get('operation_type', '')  # 从查询字符串中获取operation_type参数
    return get_logs_list(user_name, user_identity, operation_type)


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000)
