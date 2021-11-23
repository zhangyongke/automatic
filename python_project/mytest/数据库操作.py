# -*- coding:utf-8 -*-
# Time:2021/11/23 21:26
# Author:zyk
# FileName:数据库操作.py
# SoftWare:PyCharm


"""操作数据库主要使用pymysql库，使用pip功能进行安装"""
import pymysql
# 打开数据库连接,填写相关的数据库连接信息，
db = pymysql.connect(user='root', passwd='root', host='192.168.1.70', database='mytestdb', port=3306, charset='utf-8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# sql插入语句
sql = "INSERT INTO employee(name, age, sex, income) values ('王五1', 25, 'F', 5000 )"
# 数据库更新语句
sql = "update employee set age = '%d' where id = '%s'" % (28, 1)
# 数据库删除语句
sql = "delete from employee where id ='%s'" %(1)
try:
    # 执行语句
    cursor.execute(sql)
    db.commit()
except Exception as e:
    # 如果发生错误则回滚
    print(e)
    db.rollback()
finally:
    # 关闭连接
    db.close()


# 数据库批量插入操作
# 打开数据库连接,填写相关的数据库连接信息，
# db = pymysql.connect(user='root', passwd='root', host='192.168.1.70', database='mytestdb', port=3306, charset='utf-8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# sql语句
sql = "INSERT INTO employee(name, age, sex, income) values (%s, %s, %s, %s)"
ls = []
employ1 = ('张三', 22, 'F', 5000)
employ2 = ('张三3', 23, 'M', 6000)
ls.append(employ1)
ls.append(employ2)
try:
    # 执行语句
    cursor.executemany(sql, ls)
    db.commit()
except Exception as e:
    # 如果发生错误则回滚
    print(e)
    db.rollback()
finally:
    # 关闭连接
    db.close()

# 数据库查询操作
# 打开数据库连接,填写相关的数据库连接信息，
db = pymysql.connect(user='root', passwd='root', host='192.168.1.70', database='mytestdb', port=3306, charset='utf-8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# sql查询语句
sql = "select * from employee where income > '%d'" % 2000
try:
    # 执行语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        id = row(0)
        name = row(1)
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("id = %d, name= %s, age= %d, sex=%s, income=%s" % (id, name, age, sex, income))
except Exception as e:
    # 如果发生错误则回滚
    print(e)
finally:
    # 关闭连接
    db.close()