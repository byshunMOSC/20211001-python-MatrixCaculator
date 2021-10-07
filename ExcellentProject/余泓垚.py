def listplus(a, b):
    c = a
    for i in range(len(a)):
        c[i] += b[i]
    return c


def listminus(a, b, mul):
    c = a
    for i in range(len(a)):
        c[i] -= b[i] * mul
    return c


def listcopy_2(a):
    out = []
    for i in range(len(a)):
        t = []
        t.extend(a[i])
        out.append(t)
    return out


class Matrix(object):
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def matrix_input(self):
        mat = []
        for i in range(self.m):
            print('输入第%d行数据：' % (i + 1),end="")
            newline = input().split()
            length = len(newline)
            if length != self.n:
                raise ValueError('length wrong')
            for j in range(length):
                newline[j] = int(newline[j])
            mat.append(newline)
        self.Mat = mat

    def __add__(self, a):
        if not isinstance(a, Matrix):
            raise ValueError('not matrix')
        if self.m != a.m or self.n != a.n:
            raise ValueError('cannot plus')
        out = Matrix(self.m, self.n)
        outlist = []
        for i in range(self.m):
            newline = []
            for j in range(self.n):
                newline.append(self.Mat[i][j] + a.Mat[i][j])
            outlist.append(newline)
        out.Mat = outlist
        return out

    def __mul__(self, a):
        if not isinstance(a, (Matrix, int, float)):
            raise TypeError('not matrix')
        if isinstance(a, Matrix):
            if self.n != a.m:
                raise ValueError('cannot multi')
            out = Matrix(self.m, a.n)
            outlist = []
            for i in range(self.m):
                newline = []
                for j in range(a.n):
                    elem = 0
                    for k in range(self.n):
                        elem += self.Mat[i][k] * a.Mat[k][j]
                    newline.append(elem)
                outlist.append(newline)
            out.Mat = outlist
            return out
        else:
            out = Matrix(self.m,self.n)
            out.Mat=listcopy_2(self.Mat)
            for i in range(self.m):
                for j in range(self.n):
                    out.Mat[i][j] *= a
            return out

    def det(self):
        if self.m != self.n:
            raise ValueError('not square matrix')
        count = 0
        for i in range(self.m):
            if self.Mat[i][0] == 0:
                count += 1
        if count == self.m:
            return 0
        else:
            temp = Matrix(self.m, self.n)
            temp.Mat = listcopy_2(self.Mat)
            for i in range(temp.m):
                for j in range(i + 1, temp.m):
                    if temp.Mat[j][i] == 0 and temp.Mat[i][i] == 0:
                        continue
                    elif temp.Mat[i][i] == 0:
                        temp.Mat[i] = listplus(temp.Mat[i], temp.Mat[j])
                    temp.Mat[j] = listminus(temp.Mat[j], temp.Mat[i], temp.Mat[j][i] / temp.Mat[i][i])
            out = 1
            for i in range(temp.m):
                out *= temp.Mat[i][i]
            return out

    def transposed(self):
        out = Matrix(self.n, self.m)
        out.Mat = []
        for i in range(self.n):
            newls = []
            for j in range(self.m):
                newls.append(self.Mat[j][i])
            out.Mat.append(newls)
        return out

    def minor(self, i, j):
        out = Matrix(self.m - 1, self.n - 1)
        out.Mat = listcopy_2(self.Mat)
        out.Mat.pop(i)
        # print(self.Mat)
        for n in range(self.m - 1):
            out.Mat[n].pop(j)
        a = out.det()
        # print(self.Mat)
        return ((-1) ** (i + j)) * a

    def inversion(self):
        if self.m != self.n:
            raise ValueError('not square matrix')
        a = self.det()
        if abs(a) < 1e-6:
            print('no inversion')
            return self
        else:
            out = Matrix(self.m, self.n)
            out.Mat = listcopy_2(self.Mat)
            for i in range(self.m):
                for j in range(self.n):
                    out.Mat[i][j] = self.minor(i, j)
            out = out * (1 / a)
            return out
    def matrix_print(self):
        for i in range(self.m):
            for j in range(self.n):
                print(self.Mat[i][j],end=" ")
            print()


def f(dic):
    a = input('定义矩阵输入矩阵名，0加法，1乘法，2数乘，3求行列式，4转置，5求逆：')
    if a == '0':
        x=input('输入实现加法的两个矩阵：').split()
        if len(x) !=2:
            raise ValueError('input error')
        if dic.get(x[0]) and dic.get(x[1]):
            (dic[x[0]]+dic[x[1]]).matrix_print()
        else:
            raise ValueError('input error')

    elif a == '1':
        x = input('输入实现矩阵乘法的两个矩阵：').split()
        if len(x) != 2:
            raise ValueError('input error')
        if dic.get(x[0]) and dic.get(x[1]):
            (dic[x[0]]*dic[x[1]]).matrix_print()
        else:
            raise ValueError('input error')

    elif a=='2':
        x = input('输入实现数乘的数字和矩阵：').split()
        if len(x) != 2:
            raise ValueError('input error')
        if dic.get(x[1]) and isinstance(x[0],(int,float)):
            (dic[x[1]]*x[0]).matrix_print()
        else:
            raise ValueError('input error')
    elif a=='3':
        x=input('请输入实现行列式计算的矩阵：')
        if dic.get(x):
            print(dic[x].det())
        else:
            raise ValueError('input error')
    elif a=='4':
        x = input('请输入实现转置的矩阵：')
        if dic.get(x):
            (dic[x].transposed()).matrix_print()
        else:
            raise ValueError('input error')
    elif a=='5':
        x = input('请输入实现求逆的矩阵：')
        if dic.get(x):
            (dic[x].inversion()).matrix_print()
        else:
            raise ValueError('input error')

    else:
        m = int(input('矩阵行数：'))
        n = int(input('矩阵列数：'))
        b = Matrix(m, n)
        dic[a] = b
        b.matrix_input()


if __name__ == '__main__':
    print('所有数据之间用空格间隔')
    dic={}
    while True:
        f(dic)