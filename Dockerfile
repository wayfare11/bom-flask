# 使用官方的 Python 镜像作为基础镜像
FROM python:3.9.19

# 安装 cron
RUN apt-get update && apt-get install -y cron

# 设置工作目录
WORKDIR /app

# 复制项目的依赖文件（比如 requirements.txt）到工作目录
COPY requirements.txt requirements.txt

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目的所有文件到工作目录
COPY . .

# 设置环境变量
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# 暴露 Flask 默认端口
EXPOSE 5000

# 复制并添加清理脚本
COPY clean_saveExcel.sh /usr/local/bin/clean_saveExcel.sh
RUN chmod +x /usr/local/bin/clean_saveExcel.sh

# 添加 cron 任务
RUN echo "0 0 * * * /usr/local/bin/clean_saveExcel.sh" > /etc/cron.d/clean_saveExcel
RUN chmod 0644 /etc/cron.d/clean_saveExcel
RUN crontab /etc/cron.d/clean_saveExcel

# 启动 cron 服务和 Flask 应用
CMD ["sh", "-c", "cron && flask run"]
