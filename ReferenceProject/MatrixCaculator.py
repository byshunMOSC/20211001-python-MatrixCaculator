import time
import numpy as np

# 对两个矩阵进行操作的计算工具类
class MatCal:
    def __init__(self, mat1C, mat2C):
        self.__mat1 = mat1C.mat
        self.__mat2 = mat2C.mat

    def add(self):
        if self.__mat1.shape != self.__mat2.shape:
            print("两个待相加矩阵的shape不一致，无法操作")
            return None
        else:
            return self.__mat1 + self.__mat2

    def multi(self):
        """矩阵对应相乘"""
        if self.__mat1.shape != self.__mat2.shape:
            print("两个待相乘矩阵的shape不满足要求，无法操作")
            return None
        return self.__mat1 * self.__mat2

    def matmulti(self):
        """矩阵相乘"""
        if self.__mat1.shape[1] != self.__mat2.shape[0]:
            print("两个待相乘矩阵的shape不满足要求，无法操作")
            return None
        return np.matmul(self.__mat1, self.__mat2)

    def sub(self):
        """矩阵相减"""
        if self.__mat1.shape != self.__mat2.shape:
            print("两个待相减矩阵的shape不满足要求，无法操作")
            return None
        return self.__mat1 - self.__mat2

    def divide(self):
        """矩阵相减"""
        if self.__mat1.shape != self.__mat2.shape:
            print("两个待相除矩阵的shape不满足要求，无法操作")
            return None
        return self.__mat1 / self.__mat2

#定义一个矩阵类，包含对自己的操作
class MatCom:
    def __init__(self):
        self.mat = 0
        self.new = True

    def change(self, mat):
        self.mat = mat
        self.new = False

    def det(self):
        """计算行列式"""
        if self.mat.shape[0] != self.mat.shape[1]:
            print("矩阵行列数目应该相等")
            return None
        return np.linalg.det(self.mat)

    def invert(self):
        """计算逆矩阵"""
        if self.det() != None and self.det() != 0:
            return np.linalg.inv(self.mat)
        else:
            return None

    def trans(self):
        """矩阵的转置"""
        return self.mat.T

    def __str__(self):
        print("----start----")
        for i in range(self.mat.shape[0]):
            for j in range(self.mat.shape[1]):
                print("\t{:.1f}".format(self.mat[i][j]), end="")
            print()
        return "----end----"

#制作一个矩阵
def mkMat():
    row, col = int(input("请输入矩阵的行数:")), int(input("请输入矩阵的列数:"))
    """根据row，col进行矩阵的构造"""
    print("----start----")
    arr = []
    for i in range(row):
        tmp_arr = []
        r = input("请输入第{:d}行内容:".format(i + 1))
        tmp = r.split()
        while len(tmp) != col:
            print("您输入尺寸大小不正确，长度应该为:{:d}".format(col))
            r = input("请输入第{:d}行内容:".format(i + 1))
            tmp = r.split()
        for j in range(col):
            tmp_arr.append(float(tmp[j]))
        arr.append(tmp_arr)
    print("----end----")
    return np.array(arr, dtype=np.float32)

def show2Res(mat1, mat2, mat):
    print("矩阵:")
    print(mat1)
    print("和矩阵:")
    print(mat2)
    print("运算结果为:")
    print(mat)


if __name__ == "__main__":
    MatList=[MatCom(),MatCom(),MatCom(),MatCom(),MatCom(),MatCom(),MatCom(),MatCom(),MatCom(),MatCom()] #记录所有定义的矩阵
    str1="sadf{}125\\\\a{}sd{:.2f}".format(33,{},165.6542)
    str2="sadf{}125\\\\a{{}}sd{:.2f}".format(33,165.6542)
    str = "请输入想要的操作对应序号：\n 0. 定义矩阵 \n 1. 显示所有矩阵 \n 2. 转置矩阵 \n 3. 行列式计算 \n 4. 逆矩阵计算 \n 5. 矩阵相加 \n 6. 矩阵相减 \n 7. 矩阵相乘 \n 8. 矩阵对应相乘 \n 9. 矩阵相除 \n 10. 矩阵对应相乘 \n 11. 退出 \n 请输入："
    x=[1,2,3]
    x[0:0]=[3,]
    print(x)
    while True:
        print(str1)
        print(str2)
        a = input(str1)

        if a == "0":
            num=int(int(input("输入要定义的矩阵编号0~9：")))
            MatList[num].change(mkMat())
            print("你定义的第%d号矩阵为：" % (num))
            print(MatList[num])

        elif a == "1":
            for n in range(10):
                if not MatList[n].new:
                    print("第%d号矩阵为："% (n))
                    print(MatList[n])
                else:
                    print("第%d号矩阵未定义" % (n))

        elif a == "2":
            num=int(input("请输入需要获得转置的矩阵编号："))
            if not MatList[num].new:
                tmp=MatList[num].trans()
                print("该矩阵的转置为:")
                print(tmp)
            else:
                print("输入错误")
                continue
            num = int(input("请输入需要被赋值的矩阵编号，输入-1可不赋值："))
            if num != -1:
                MatList[num].change(tmp)

        elif a == "3":
            num = int(input("请输入需要计算行列式的矩阵编号："))
            if MatList[num].det() != None:
                print("矩阵：")
                print(MatList[num])
                print("的行列式值为：{:.2f}".format(MatList[num].det()))
            else:
                print("输入错误")

        elif a == "4":
            num = int(input("请输入需要获取逆矩阵的矩阵编号："))
            if MatList[num].invert().all() != None:
                print("矩阵：")
                print(MatList[num])
                print("的逆矩阵为")
                tmp=MatList[num].invert()
                print(tmp)
            else:
                print("不可求逆！")
                continue
            num = int(input("请输入需要被赋值的矩阵编号，输入-1可不赋值："))
            if num != -1:
                MatList[num].change(tmp)

        elif a == "5":
            num = input("请输入需要相加的两个矩阵的矩阵编号：").split()
            num[0],num[1]=int(num[0]),int(num[1])
            tmp = MatCal(MatList[num[0]], MatList[num[1]])
            if tmp != None:
                tmp2=tmp.add()
                show2Res(MatList[num[0]], MatList[num[1]], tmp2)
            num = int(input("请输入需要被赋值的矩阵编号，输入-1可不赋值："))
            if num != -1:
                MatList[num].change(tmp2)

        elif a == "6":
            num = input("请输入需要相减的两个矩阵的矩阵编号：").split()
            num[0], num[1] = int(num[0]), int(num[1])
            tmp = MatCal(MatList[num[0]], MatList[num[1]])
            if tmp != None:
                tmp2=tmp.sub()
                show2Res(MatList[num[0]], MatList[num[1]], tmp2)
            num = int(input("请输入需要被赋值的矩阵编号，输入-1可不赋值："))
            if num != -1:
                MatList[num].change(tmp2)

        elif a == "7":
            num = input("请输入需要相乘的两个矩阵的矩阵编号：").split()
            num[0], num[1] = int(num[0]), int(num[1])
            tmp = MatCal(MatList[num[0]], MatList[num[1]])
            if tmp != None:
                tmp2=tmp.matmulti()
                show2Res(MatList[num[0]], MatList[num[1]], tmp2)
            num = int(input("请输入需要被赋值的矩阵编号，输入-1可不赋值："))
            if num != -1:
                MatList[num].change(tmp2)

        elif a == "8":
            num = input("请输入需要对应相乘的两个矩阵的矩阵编号：").split()
            num[0], num[1] = int(num[0]), int(num[1])
            tmp = MatCal(MatList[num[0]], MatList[num[1]])
            if tmp != None:
                tmp2=tmp.multi()
                show2Res(MatList[num[0]], MatList[num[1]], tmp2)
            num = int(input("请输入需要被赋值的矩阵编号，输入-1可不赋值："))
            if num != -1:
                MatList[num].change(tmp2)

        elif a == "9":
            num = input("请输入需要相除的两个矩阵的矩阵编号：").split()
            num[0], num[1] = int(num[0]), int(num[1])
            tmp = MatCal(MatList[num[0]], MatList[num[1]])
            if tmp != None:
                tmp2=tmp.divide()
                show2Res(MatList[num[0]], MatList[num[1]], tmp2)
            num = int(input("请输入需要被赋值的矩阵编号，输入-1可不赋值："))
            if num != -1:
                MatList[num].change(tmp2)

        elif a == "10":
            num = input("请输入需要对应相除的两个矩阵的矩阵编号：").split()
            num[0], num[1] = int(num[0]), int(num[1])
            tmp = MatCal(MatList[num[0]], MatList[num[1]])
            if tmp != None:
                tmp2=tmp.divimultide()
                show2Res(MatList[num[0]], MatList[num[1]], tmp.tmp2())
            num = int(input("请输入需要被赋值的矩阵编号，输入-1可不赋值："))
            if num != -1:
                MatList[num].change(tmp2)

        elif a == "11":
            break

        else:
            print("在搞什么")

        time.sleep(1)
