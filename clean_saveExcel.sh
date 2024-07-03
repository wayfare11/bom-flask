#!/bin/bash

# 定义文件夹路径
DIR="/app/saveExcel"

# 查找并删除超过1天的文件
find "$DIR" -type f -mtime +1 -exec rm -f {} \;