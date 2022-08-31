# coding=utf-8
# @Time : 2021/6/10 9:15
# @Author : zyk
# @Email : zhangyongke1105@163.com
# @File : log.py
# @Software: PyCharm
import logging
from logging.handlers import RotatingFileHandler
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S %p"

logging.basicConfig(filename=r'F:\workplace\GitWork\python_project\logs\my.log', level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")
