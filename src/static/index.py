from js import window
from pyodide.ffi import create_proxy 
import os
import sys
from main import main
from main import start
# 简单加法函数
def py_main(A, B):
    C=main(A, B)
    return C

def py_start():
    start();
    return


window.PyMain = create_proxy(py_main);
window.PyStart = create_proxy(py_start);

print("根目录:", os.listdir("/"))
print("home:", os.listdir("/home"))
print("当前目录:", os.listdir("."))


