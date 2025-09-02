from utils import window


# https://blog.csdn.net/qq_26074053/article/details/101909847
# 与运算（二输入）：A、B均为True（按下）时返回True，否则False
def jing_and(A, B):
    return A and B


# 或运算（二输入）：A、B任一为True（按下）时返回True，否则False
def jing_or(A, B):
    return A or B


# 非运算（单输入）：返回A的相反值（按下↔未按下）
def jing_not(A):
    return not A


# 与非运算（二输入）：先算A、B与运算，再取反
def jing_nand(A, B):
    return not (A and B)


# 异或运算（二输入）：A、B状态不同（一按一未按）时返回True，否则False
def jing_xor(A, B):
    return A^B


# 同或运算（二输入）：A、B状态相同（一按一按或一未按一按）时返回True，否则False
def jing_xnor(A, B):
    return A==B

# 主函数：接收按键A/B状态，默认返回或运算结果（控制灯泡亮灭：True=亮）
def main(A, B):
    return jing_or(A, B)



def start():
    print("AAAAAAAAAA")
    c= jing_and(1,1)
    window.alert(c)
    return

# 测试（可选）：验证函数逻辑
if __name__ == "__main__":
    # 测试输入：A按下（True），B未按下（False）
    A, B = True, False
    print(f"A={A}, B={B}")
    print(f"与：{jing_and(A,B)} | 或：{jing_or(A,B)} | 异或：{jing_xor(A,B)}")