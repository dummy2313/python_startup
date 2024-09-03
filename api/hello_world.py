# -*- coding: UTF-8 -*-
from flask import Flask    # 导入Flask模块
app = Flask(__name__)      # 创建Flask实例，并指定模块名
@app.route('/')                 # 定义路由，即当访问 根目录 时返回下面的函数结果
def hello_world():
    return 'Hello, World!'   # 返回字符串Hello, World!
if __name__ == '__main__':
    app.run()                       # 运行Flask应用程序