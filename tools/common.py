"""
函数需求：MD5加密
入参：加密的明文---string类型
出参：加密的密文---string类型
"""
import hashlib


def get_md5_data(pwd: str):
    # 1.实列话md5对象
    md5 = hashlib.md5()
    # 2.调用加密操作
    md5.update(pwd.encode('utf-8'))
    # 3.返回加密后的结果16进制的结果
    return md5.hexdigest()
