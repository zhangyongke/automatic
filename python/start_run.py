# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 2:07 PM
# @Author  : zyk
# @Email   : zhangyongke1105@163.com
# @File    : start_run.py
# @Software : PyCharm

# 创建定时任务
import time
import os
k = 1
while k < 2:
    now_time = time.strftime('%H_%M')
    if now_time == '21_00':
        print("开始执行脚本")
        os.chdir("/Volumes/Ubuntu/Gitworkplace/workplace-Git/python/")    # 切换到脚本所在目录
        os.system('Python all_test.py')    # 执行脚本
        print("脚本运行完成退出")
        break
    else:
        time.sleep(10)
        print(now_time)
