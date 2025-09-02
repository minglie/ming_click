from js import window
from pyodide.ffi import create_proxy 
import os
import sys
import main

# 简单加法函数
def py_main(selectedLogic,A, B):
    if(selectedLogic==None):
       return False
    match selectedLogic:
        case "and":
            return main.jing_and(A,B)
        case "or":
            return main.jing_or(A,B)
        case "not":
            return main.jing_not(A)
        case "nand":
            return main.jing_nand(A,B)
        case "xor":
            return main.jing_xor(A,B)
        case "xnor":
            return main.jing_xnor(A,B)
        case _:
            return  False
    C=main.main(A, B)
    return C

def py_start():
    main.start();
    return


window.PyMain = create_proxy(py_main);
window.PyStart = create_proxy(py_start);

print("根目录:", os.listdir("/"))
print("home:", os.listdir("/home"))
print("当前目录:", os.listdir("."))