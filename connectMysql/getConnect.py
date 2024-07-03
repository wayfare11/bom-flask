import pymysql.cursors

# 数据库连接配置
db_config = {
    # 'host': 'host.docker.internal',
    'host': '10.16.0.15',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'database': 'bom_yinliu'
}

# 数据库连接函数
def get_database_connection():
    try:
        con = pymysql.connect(**db_config)
        return con
    except Exception as e:
        print(e)
        return None

# 示例使用
if __name__ == "__main__":
    connection = get_database_connection()
    if connection:
        print("数据库连接成功")
        connection.close()
    else:
        print("数据库连接失败")
