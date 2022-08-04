import os
import sys
os.system("title GCC 编译工具 v0.0.1 中文版 by Juruo Develop Team")
while True:
    print("【1】使用 G++ 编译")
    print("【2】使用 GCC 编译")
    print("【3】查看 G++ 版本")
    print("【4】查看 GCC 版本")
    print("【5】运行可执行文件")
    print("【0】退出编译工具")
    tp = int(input("请输入："))
    if tp == 0:
        sys.exit(0)
    elif tp == 1:
        cpp = input("请输入 C++ 源文件路径：")
        exe = input("请输入可执行文件路径：")
        ext = input("请输入编译选项：")
        os.system("g++ -o " + exe + " " + cpp + " " + ext)
    elif tp == 2:
        c = input("请输入 C 源文件路径：")
        exe = input("请输入可执行文件路径：")
        ext = input("请输入编译选项：")
        os.system("gcc -o " + exe + " " + c + " " + ext)
    elif tp == 3:
        os.system("g++ -v")
    elif tp == 4:
        os.system("gcc -v")
    elif tp == 5:
        exe = input("请输入可执行文件路径：")
        os.system(exe)
