# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Hiuhung Wan
 
import os
from time import time
 
dir_count = 0
file_count = 0
 
def get_all_dir(path, sp = "|"):
    # 得到当前目录下所有的文件
    fills_list = os.listdir(path)
 
    sp += "-"
    # 处理每一个文件
    for file_name in fills_list:
 
        # 判断是否是路径（用绝对路径）
        file_abs_path = os.path.join(path, file_name)
        if os.path.isdir(file_abs_path):
            global dir_count    # 写了这个global，不知道会不会被开除
            dir_count += 1
            print(sp, "目录：",file_name)
            get_all_dir(file_abs_path, sp)
        else:
            global file_count
            file_count += 1
            print(sp, "普通文件：",file_name)
 
def main():
 
 
    # user_dir = r"D:\Py\1704"
    user_dir = r"C:\Python36"
    t1 = time()
    get_all_dir(user_dir)
    t2 = time()
 
    print("一共有%d个目录，%d个文件，耗时%.3f秒" % (dir_count, file_count, t2 - t1))
 
if __name__ == "__main__":
    main()