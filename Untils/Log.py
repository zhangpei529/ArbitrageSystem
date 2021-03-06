from logging.handlers import TimedRotatingFileHandler
import logging
import datetime
import sys

# 日志配置
# 获取logger实例，如果参数为空则返回root logger
log = logging.getLogger()
# 指定logger输出格式
formatter = logging.Formatter('%(asctime)s  %(module)s  %(funcName)s  %(levelname)-8s:'
                              '%(message)s')
# 文件日志
# file_handler = logging.FileHandler("%s-%s-%s.log" % (datetime.datetime.now().year,
#                                                      datetime.datetime.now().month,
#                                                      datetime.datetime.now().day))
file_handler = TimedRotatingFileHandler(filename="logs/%s-%s-%s.log" % ( datetime.datetime.now(
    ).year, datetime.datetime.now().month, datetime.datetime.now().day), when="D", interval=1,
                                        backupCount=30)
file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter
# 为logger添加的日志处理器
log.addHandler(file_handler)
log.addHandler(console_handler)
# 指定日志的最低输出级别，默认为WARN级别
log.setLevel(logging.INFO)
