import mysql.connector
from mysql.connector import errorcode

# 数据库连接配置
config = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'database': 'yinliu',
    'raise_on_warnings': True
}

# 创建连接
try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # 创建表的 SQL 语句
    create_table_query = (
        "CREATE TABLE IF NOT EXISTS operation_logs ("
        "  log_id INT AUTO_INCREMENT PRIMARY KEY,"
        "  username TEXT NOT NULL,"
        "  user_role TEXT NOT NULL,"
        "  action TEXT NOT NULL,"
        "  content TEXT NOT NULL,"
        "  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
        ") ENGINE=InnoDB"
    )

    # 执行创建表的语句
    cursor.execute(create_table_query)
    print("Table 'operation_logs' created successfully.")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    # 关闭游标和连接
    cursor.close()
    cnx.close()
