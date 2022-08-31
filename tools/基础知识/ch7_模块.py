# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 20:59
# @Author  : zyk
# @FileName: ch7_模块.py
# @Software: PyCharm
# @Email ：zhangyongke1105@163.com

# time模块
import time
# 格式化日期的格式为年-月-日 时：分：秒
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# python中时间日期格式化符号format如下：
"""
%y：两位数的年份表示
%Y：四位数的年份表示
%m：月份（01~12）
%d：月内中的一天（01~31）
%H：24小时制小时数（0~23）
%I：12小时制小时数
%M：分钟数（00~59）
%S：秒（00~59）
"""


# os模块
# python使用os模块来处理文件和目录，不受平台限制
# （1）os.popen()方法用于从一个命令打开一个管道，在Linux，windows中有效，其格式如下：os.popen(command),command:要使用的命令
# 例如linux系统通过iostat命令查看系统的I/O状态信息，从而确定I/O性能是否存在瓶颈，
# （2）os.listdir()方法用于返回指定的文件夹包含的文件和目录的名称列表，其格式如下：os.listdir(path)，path：需要列出的目录路径。如果不指定
# path参数，列出的是执行脚本目录下的文件和目录的列表，例如输出D盘下的所有文件和目录的名称列表
import os
dirs = os.listdir("D:/")
print(dirs)



