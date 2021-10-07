import copy

#分解质因数
def breakdown(num):
    result = {}
    i = 2
    numc = num
    counter = 0
    while i <= numc:
        if numc % i == 0:
            counter += 1
            numc /= i
        else:
            if counter != 0:
                result[i] = counter
            i += 1
            counter = 0
    result[i] = counter
    return result

#找出最小公倍数
def min_com_multi(a, b):
    factors_a = breakdown(a)
    factors_b = breakdown(b)
    list_a = factors_a.keys()
    for i in list_a:
        if i in factors_b:
            if factors_a[i] < factors_b[i]:
                factors_a.pop(i)
            else:
                factors_b.pop(i)
    factors_a.update(factors_b)
    result = 1
    for i in list_a:
        while factors_a[i] != 0:
            result *= i
            factors_a[i] -= 1
    return result

#找出最大公因数
def max_com_factor(a, b):
    factors_a = breakdown(a)
    factors_b = breakdown(b)
    list_a = factors_a.keys()
    for i in list_a:
        if i in factors_b:
            factors_a[i] = min(factors_a[i], factors_b[i])
        else:
            factors_a[i] = 0
    result = 1
    for i in list_a:
        while factors_a[i] != 0:
            result *= i
            factors_a[i] -= 1
    return result

'''
————————————————————————————————————————————————————————————————————————
定义分数类，用于弥补计算机浮点数在运算中由精度不足引起的损失
————————————————————————————————————————————————————————————————————————
'''
class FRA:
    numerator = 0
    denominator = 1
    symbol = ''
#初始化分数
    def __init__(self, num):
        if type(num) == int:
            if num < 0:
                self.symbol = '-'
                num = abs(num)
            self.numerator = num
        elif type(num) == float:
            if num < 0:
                self.symbol = '-'
                num = abs(num)
            mid = str(num)
            mid_len = len(mid)
            point_place = mid.find('.')
            mid = mid.replace('.', '')
            self.numerator = int(mid)
            self.denominator = 10 ** (mid_len - 1 - point_place)
        elif type(num) == str:
            if num[0] == '-':
                num = num.replace('-', '', 1)
                self.symbol = '-'
            temp = copy.deepcopy(num)
            temp = temp.replace('.', '', 1)
            if temp.isnumeric():
                point_place = num.find('.')
                if point_place == -1:
                    self.numerator = int(num)
                else:
                    self.numerator = int(temp)
                    self.denominator = 10 ** (len(num) - 1 - point_place)
            else:
                temp = temp.replace('/', '', 1)
                if temp.isnumeric():
                    self.numerator, self.denominator = map(int, num.split('/', 1))
                    if self.denominator == 0:
                        raise Exception("分母不能为零！")
                else:
                    raise Exception("错误的输入！")  
        self.reduct()
#约分
    def reduct(self):
        if (self.numerator == 0):
            self.symbol = ''
            self.denominator = 1
        elif self.numerator < 0 and self.symbol == '-':
            self.numerator = -self.numerator
            self.symbol = ''
        elif self.numerator < 0 and self.symbol == '':
            self.numerator = -self.numerator
            self.symbol = '-'
        MAX_com_factor = max_com_factor(self.denominator, self.numerator)
        self.numerator //= MAX_com_factor
        self.denominator //= MAX_com_factor
#返回分数的小数近似值
    def f(self):
        return self.numerator / self.denominator
#重写print打印分数的方式
    def __repr__(self, length = 0):
        if self.denominator == 1:
            return "%s%d" % (self.symbol, self.numerator)
        return "%s%d/%d" % (self.symbol, self.numerator, self.denominator)
#重载格式化输出
    def __format__(self):
        return self.__repr__()
#临时符号化分数，用于计算
    def symbolize(self):
        if self.symbol == '-':
            self.numerator = -self.numerator
#重写分数的加法
    def __add__(self, other):
        if type(other) == FRA:
            result = copy.deepcopy(self)
            result.symbol = ''
            mid1 = copy.deepcopy(self)
            mid2 = copy.deepcopy(other)
            mid1.symbolize()
            mid2.symbolize()
            result.denominator = mid1.denominator * mid2.denominator
            result.numerator = mid1.denominator * mid2.numerator + mid1.numerator * mid2.denominator
            result.reduct()
            return result
        if type(other) == float or type(other) == int or type(other) == str:
            return FRA(other) + self
        else:
            raise Exception("对分数进行了非法操作！")
#重写分数的右侧加法
    def __radd__(self, other):
        if type(other) == FRA:
            result = copy.deepcopy(self)
            result.symbol = ''
            mid1 = copy.deepcopy(self)
            mid2 = copy.deepcopy(other)
            mid1.symbolize()
            mid2.symbolize()
            result.denominator = mid1.denominator * mid2.denominator
            result.numerator = mid1.denominator * mid2.numerator + mid1.numerator * mid2.denominator
            result.reduct()
            return result
        if type(other) == float or type(other) == int or type(other) == str:
            return FRA(other) + self
        else:
            raise Exception("对分数进行了非法操作！")
#重写分数的减法
    def __sub__(self, other):
        if type(other) == FRA:
            result = copy.deepcopy(self)
            result.symbol = ''
            mid1 = copy.deepcopy(self)
            mid2 = copy.deepcopy(other)
            mid1.symbolize()
            mid2.symbolize()
            result.denominator = mid1.denominator * mid2.denominator
            result.numerator = mid1.numerator * mid2.denominator - mid1.denominator * mid2.numerator
            result.reduct()
            return result
        if type(other) == float or type(other) == int or type(other) == str:
            return self - FRA(other)
        else:
            raise Exception("对分数进行了非法操作！")
#重写分数的右侧减法
    def __rsub__(self, other):
        if type(other) == FRA:
            result = copy.deepcopy(self)
            result.symbol = ''
            mid1 = copy.deepcopy(self)
            mid2 = copy.deepcopy(other)
            mid1.symbolize()
            mid2.symbolize()
            result.denominator = mid1.denominator * mid2.denominator
            result.numerator = mid1.denominator * mid2.numerator - mid1.numerator * mid2.denominator
            result.reduct()
            return result
        if type(other) == float or type(other) == int or type(other) == str:
            if type(other) == int and other == 0:
                result = copy.deepcopy(self)
                if result.symbol == '-':
                    result.symbol = ''
                    return result
                elif result.symbol == '' and result.numerator == 0:
                    return result
                else:
                    result.symbol = '-'
                    return result
            return FRA(other) - self
        else:
            raise Exception("对分数进行了非法操作！")
#重载相反数运算符
    def __neg__(self):
        result = copy.deepcopy(self)
        if result.symbol == '-':
            result.symbol = ''
            return result
        elif result.symbol == '' and result.numerator == 0:
            return result
        else:
            result.symbol = '-'
            return result
    def __mul__(self, other):
        if type(other) == FRA:
            result = copy.deepcopy(self)
            result.symbol = ''
            mid1 = copy.deepcopy(self)
            mid2 = copy.deepcopy(other)
            mid1.symbolize()
            mid2.symbolize()
            result.denominator = mid1.denominator * mid2.denominator
            result.numerator = mid1.numerator * mid2.numerator
            result.reduct()
            return result
        if type(other) == float or type(other) == int or type(other) == str:
            return FRA(other) * self
        else:
            raise Exception("对分数进行了非法操作！")
#重载右侧乘法运算符
    def __rmul__(self, other):
        if type(other) == FRA:
            result = copy.deepcopy(self)
            result.symbol = ''
            mid1 = copy.deepcopy(self)
            mid2 = copy.deepcopy(other)
            mid1.symbolize()
            mid2.symbolize()
            result.denominator = mid1.denominator * mid2.denominator
            result.numerator = mid1.numerator * mid2.numerator
            result.reduct()
            return result
        if type(other) == float or type(other) == int or type(other) == str:
            return FRA(other) * self
        else:
            raise Exception("对分数进行了非法操作！")
#重载除法运算符
    def __truediv__(self, other):
        if type(other) == FRA:
            if other.numerator == 0:
                raise Exception("不能除以0！")
            result = copy.deepcopy(self)
            result.symbol = ''
            mid1 = copy.deepcopy(self)
            mid2 = copy.deepcopy(other)
            mid1.symbolize()
            mid2.symbolize()
            result.denominator = mid1.denominator * mid2.numerator
            result.numerator = mid1.numerator * mid2.denominator
            if result.denominator < 0:
                result.denominator = -result.denominator
                result.numerator = -result.numerator
            result.reduct()
            return result
        if type(other) == float or type(other) == int or type(other) == str:
            return self / FRA(other)
        else:
            raise Exception("对分数进行了非法操作！")
#重载右侧除法运算符
    def __rtruediv__(self, other):
        if type(other) == FRA:
            if other.numerator == 0:
                raise Exception("不能除以0！")
            result = copy.deepcopy(self)
            result.symbol = ''
            mid1 = copy.deepcopy(self)
            mid2 = copy.deepcopy(other)
            mid1.symbolize()
            mid2.symbolize()
            result.denominator = mid2.denominator * mid1.numerator
            result.numerator = mid2.numerator * mid1.denominator
            if result.denominator < 0:
                result.denominator = -result.denominator
                result.numerator = -result.numerator
            result.reduct()
            return result
        if type(other) == float or type(other) == int or type(other) == str:
            return FRA(other) / self
        else:
            raise Exception("对分数进行了非法操作！")
#重载>、<运算符
    def __gt__(self, other):
        if (other - self).symbol == '-':
            return True
        else:
            return False
    def __lt__(self, other):
        if (self - other).symbol == '-':
            return True
        else:
            return False
#重载==、!=运算符
    def __eq__(self, other):
        if (self - other).numerator == 0:
            return True
        else:
            return False
    def __ne__(self, other):
        if (self - other).numerator != 0:
            return True
        else:
            return False
#重载>=、<=运算符
    def __ge__(self, other):
        mid = self - other
        if mid.symbol == '-':
            return False
        else:
            return True
    def __le__(self, other):
        mid = other - self
        if mid.symbol == '-':
            return False
        else:
            return True
        


#创建单位n阶矩阵
def E(n):
    result = MATRIX([[FRA(0) for i in range(n)] for j in range(n)])
    temp = FRA(1)
    for i in range(n):
        result.matrix[i][i] += temp
    return result


'''
————————————————————————————————————————————————————————————————————————
定义矩阵类，用于矩阵的各种运算
————————————————————————————————————————————————————————————————————————
'''
class MATRIX:
#用户输入矩阵元素以初始化矩阵
    def __init__(self, ini_matrix = []):
        if len(ini_matrix) != 0:
            self.matrix = copy.deepcopy(ini_matrix)
            self.row = len(self.matrix)
            self.column = len(self.matrix[0])
        else:
            self.row, self.column = map(int, input("输入矩阵的行数和列数(以空格间隔)：").split())
            if self.row <= 0 or self.column <= 0:
                raise Exception("你是故意找茬是不是！？")
            print("逐行输入矩阵，元素之间用空格分隔：\n")
            self.matrix = [self.getlist(self.column) for j in range(self.row)]
            print("你输入的矩阵是：")
            print(self)
        if type(self.matrix[0][0]) != FRA:
            for i in range(self.row):
                for j in range(self.column):
                    self.matrix[i][j] = FRA(self.matrix[i][j])
#供矩阵初始化使用的函数，从用户处读取一行元素
    def getlist(self, num, type = int, seperation = ' '):
        mylist = list(input().split(seperation))
        if len(mylist) != num:
            raise Exception("你是故意找茬是不是")
        for i in range(len(mylist)):
            mylist[i] = FRA(mylist[i])
        return mylist
#供矩阵乘法运算使用的函数，计算新矩阵中单个元素
    def sin_mul(self, a, num, b, b_column):
        result = 0
        for i in range(num):
            result += a[i] * b.matrix[i][b_column]
        return result
#重载+运算符
    def __add__(self, other):
        if (self.row != other.row) or (self.column != other.column):
            raise Exception("矩阵形状不同不能相加减")
        result = copy.deepcopy(self)
        for i in range(self.row):
            for j in range(self.column):
                result.matrix[i][j] += other.matrix[i][j]
        return result
#重载-运算符
    def __sub__(self, other):
        if (self.row != other.row) or (self.column != other.column):
            raise Exception("矩阵形状不同不能相加减")
        result = copy.deepcopy(self)
        for i in range(self.row):
            for j in range(self.column):
                result.matrix[i][j] -= other.matrix[i][j]
        return result
#重载*运算符（数左乘矩阵运算）
    def __rmul__(self, num):
        if type(num) == int or type(num) == float or type(num) == str:
            a = FRA(num)
            result = copy.deepcopy(self)
            for i in range(self.row):
                for j in range(self.column):
                    result.matrix[i][j] *= a
            return result
        elif type(num) == FRA:
            result = copy.deepcopy(self)
            for i in range(self.row):
                for j in range(self.column):
                    result.matrix[i][j] *= num
            return result
        else:
            raise Exception("不要对矩阵做奇怪的乘法！")
#重载*运算符（数右乘矩阵运算以及矩阵乘法）
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            result = copy.deepcopy(self)
            a = FRA(other)
            for i in range(self.row):
                for j in range(self.column):
                    result.matrix[i][j] *= a
            return result
        elif type(other) == FRA:
            result = copy.deepcopy(self)
            for i in range(self.row):
                for j in range(self.column):
                    result.matrix[i][j] *= other
            return result
        elif type(other) == MATRIX:
            if self.column == other.row:
                result = MATRIX([[self.sin_mul(self.matrix[j], self.row, other, i) for i in range(other.column)] for j in range(self.row)])
                return result
            else:
                raise Exception("这俩矩阵不可乘")
        else:
            raise Exception("不要对矩阵做奇怪的乘法！")
#重载print()调用
    def __repr__(self):
        mystr = ""
        length = {i: 0 for i in range(self.column)}
        for j in range(self.column):
            for i in range(self.row):
                if length[j] < len(self.matrix[i][j].__repr__()):
                    length[j] = len(self.matrix[i][j].__repr__())
        for i in range(self.row):
            if i == 0:
                mystr += "  ╭"
            elif i == self.row - 1:
                mystr += "  ╰"
            else:
                mystr += "  │"

            for j in range(self.column):
                mystr += ' {0: ^{1}} '.format(self.matrix[i][j].__repr__(), length[j])

            if i == 0:
                mystr += "╮\n"
            elif i == self.row - 1:
                mystr += "╯\n"
            else:
                mystr += "│\n"
        return mystr
#内置一个print函数以备不时之需
    def print(self):
        for i in range(self.row):
            if i == 0:
                print("     ╭", end = '')
            elif i == self.row - 1:
                print("     ╰", end = '')
            else:
                print("     │", end = '')

            for j in range(self.column):
                print("{:^5d}".format(self.matrix[i][j]), end = '')

            if i == 0:
                print("╮")
            elif i == self.row - 1:
                print("╯")
            else:
                print("│")
#计算矩阵的转置
    def T(self):
        for i in range(self.row):
            for j in range(self.column):
                result = MATRIX([[copy.deepcopy(self.matrix[i][j]) for i in range(self.row)] for j in range(self.column)])
        return result
#对矩阵某行或某列作K倍处理，默认情况下作行变换
    def k_trans(self, direction, line_num, k):
        result = copy.deepcopy(self)
        if direction == 'r':
            if line_num <= self.row and line_num > 0:
                for i in range(self.column):
                    result.matrix[line_num - 1][i] *= k
            else:
                raise Exception("索引溢出！")
        elif direction == 'c':
            if line_num <= self.column and line_num > 0:
                for i in range(self.row):
                    result.matrix[i][line_num - 1] *= k
        else:
            raise Exception("第二个参数要为'r'或'c'")
        return result
#将矩阵某行（列）的k倍加到另一行（列）上
    def kplus_trans(self, direction, origin, k, goal):
        result = copy.deepcopy(self)
        if direction == 'r':
            if origin <= self.row and origin > 0 and goal <= self.row and goal > 0:
                for i in range(self.column):
                    result.matrix[goal - 1][i] = result.matrix[goal - 1][i] + result.matrix[origin - 1][i] * k
            else:
                raise Exception("索引溢出！")
        elif direction == 'c':
            if origin <= self.row and origin > 0 and goal <= self.row and goal > 0:
                for i in range(self.row):
                    result.matrix[i][goal - 1] = result.matrix[i][goal - 1] + result.matrix[i][origin - 1] * k
        else:
            raise Exception("第二个参数要为'r'或'c'")
        return result
#交换两行（列）
    def exch_trans(self, direction, a, b):
        result = copy.deepcopy(self)
        if direction == 'r':
            if a <= self.row and a > 0 and b <= self.row and b > 0:
                for i in range(self.column):
                    result.matrix[a - 1][i] = self.matrix[b - 1][i]
                    result.matrix[b - 1][i] = self.matrix[a - 1][i]
            else:
                raise Exception("索引溢出！")
        elif direction == 'c':
            if a <= self.row and a > 0 and b <= self.row and b > 0:
                for i in range(self.row):
                    result.matrix[i][a - 1] = self.matrix[i][b - 1]
                    result.matrix[i][b - 1] = self.matrix[i][a - 1]
        else:
            raise Exception("第二个参数要为'r'或'c'")
        return result
#化行（列）阶梯矩阵，由于偷懒，列的实现就用转置实现了
    def stairs(self, special = 'S', direction = 'r'):
        result = copy.deepcopy(self)
        counter = 0
        if direction != 'r' and direction != 'c':
            raise direction("第二个参数要为'r'或'c'")
        for i in range(self.column):                    #遍历每一行
            for j in range(counter, self.row):                   #首先找到该列的非0行
                if result.matrix[j][i] != 0:
                    result = result.exch_trans('r', counter + 1, j + 1)
                    #result = result.k_trans('r', counter + 1, FRA(1) / result.matrix[counter][i])
                    break
            if result.matrix[counter][i] == 0:
                break
            else:
                for j in range(counter + 1, self.row):
                    if result.matrix[j][i] != 0:
                        result = result.kplus_trans('r', counter + 1, -result.matrix[j][i] / result.matrix[counter][i], j + 1)
            counter += (result.matrix[counter][i] != 0)
        if direction == 'c':
            result.matrix = result.T()
        if special == 'S':
            return result
        elif special == 'R':
            return counter
#求方阵的行列式
    def det(self):
        if self.row == self.column:
            result = FRA(1)
            for i in range(self.row):
                result *= self.stairs().matrix[i][i]
        else:
            raise Exception("只有方阵具有行列式")
        return result
#化行（列）最简阶梯矩阵，由于偷懒，列的实现就用转置实现了（好像这个暂且是没起到什么作用...）
    def simplest(self, direction = 'r'):
        result = copy.deepcopy(self)
        counter = 0
        if direction != 'r' and direction != 'c':
            raise direction("第二个参数要为'r'或'c'")
        for i in range(self.column):                    #遍历每一行
            for j in range(counter, self.row):                   #首先找到该列的非0行
                if result.matrix[j][i] != 0:
                    result = result.exch_trans('r', counter + 1, j + 1)
                    result = result.k_trans('r', counter + 1, FRA(1) / result.matrix[counter][i])
                    break
            if result.matrix[counter][i] == 0:
                break
            else:
                for j in range(self.row):
                    if j == counter:
                        continue
                    if result.matrix[j][i] != 0:
                        result = result.kplus_trans('r', counter + 1, -result.matrix[j][i] / result.matrix[counter][i], j + 1)
            counter += (result.matrix[counter][i] != 0)
        if direction == 'c':
            result.matrix = result.T()
        return result
#求逆矩阵
    def reverse(self, direction = 'r'):
        if self.row != self.column:
            raise Exception("非方阵不可逆！")
        result = copy.deepcopy(self)
        counter = 0
        E0 = E(self.row)
        if direction != 'r' and direction != 'c':
            raise direction("第二个参数要为'r'或'c'")
        for i in range(self.column):                    #遍历每一行
            for j in range(counter, self.row):                   #首先找到该列的非0行
                if result.matrix[j][i] != 0:
                    E0 = E0.exch_trans('r', counter + 1, j + 1)
                    result = result.exch_trans('r', counter + 1, j + 1)
                    E0 = E0.k_trans('r', counter + 1, FRA(1) / result.matrix[counter][i])
                    result = result.k_trans('r', counter + 1, FRA(1) / result.matrix[counter][i])
                    break
            if result.matrix[counter][i] == 0:
                break
            else:
                for j in range(self.row):
                    if j == counter:
                        continue
                    if result.matrix[j][i] != 0:
                        E0 = E0.kplus_trans('r', counter + 1, -result.matrix[j][i] / result.matrix[counter][i], j + 1)
                        result = result.kplus_trans('r', counter + 1, -result.matrix[j][i] / result.matrix[counter][i], j + 1)
            counter += (result.matrix[counter][i] != 0)
        if counter < result.row:
            raise Exception("该矩阵为降秩矩阵，不可逆")
        if direction == 'c':
            result.matrix = result.T()
        return E0
#求矩阵的秩
    def R(self):
        return self.stairs('R')
#求代数余子式
    def A(self, a, b):
        result = MATRIX([[self.matrix[i][j] for j in range(self.column) if (b - 1) != j] for i in range(self.row) if (a - 1) != i])
        return (-1) ** (a + b) * result.det()
#求方阵的伴随矩阵
    def companion(self):
        if self.row != self.column:
            raise Exception("只有方阵才具有伴随矩阵")
        result = MATRIX([[self.A(i + 1, j + 1) for j in range(self.column)] for i in range(self.row)])
        return result.T()
#重载矩阵除法运算符，可以除以某个数
    def __truediv__(self, other):
        if type(other) == FRA:
            return self * (1 / other)
        else:
            return self * (1 / FRA(other)) 