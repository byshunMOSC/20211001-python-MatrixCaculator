#交换两行
def switch(mat,a,b):
    temp=mat[a].copy()
    mat[a]=mat[b].copy()
    mat[b]=temp.copy()

#消去(行列式计算时用)
def cancel(mat,m,n,i,j):
    count = i+1
    while count<m:
        if i>=m:
            break
        if mat[count][j] == 0:
            count=count+1
            continue
        k=mat[count][j]/mat[i][j]
        ct=0
        while ct<n:
            mat[count][ct]=mat[count][ct]-k*mat[i][ct]
            ct=ct+1
        count=count+1


#消去(矩阵计算时用,行列式不为零)
def cancelall(mat,emat,m,n,i):
    count=0
    while count<m:
        if i>=m :
            break
        if count==i:
            count=count+1
            continue
        if mat[count][i] == 0:
            count=count+1
            continue
        k = mat[count][i] / mat[i][i]
        ct = 0
        while ct < n:
            mat[count][ct] = mat[count][ct] - k * mat[i][ct]
            emat[count][ct] = emat[count][ct] - k * emat[i][ct]
            ct = ct + 1
        count = count + 1

class Mat:
    def __init__(self,m,n,mat):
        self.m=m
        self.n=n
        self.mat=mat

#转置矩阵
    def trans(self):
        temp=[[0 for i in range(self.m)] for i in range(self.n)]
        i=0;
        while i<self.n:
            j=0
            while j<self.m:
                temp[i][j]=self.mat[j][i]
                j=j+1
            i=i+1
        return temp

#变换矩阵
    def change(self,mat):
        self.mat=mat

#计算方阵的行列式得值
    def det(self):
        count=1;
        if self.m != self.n:
            print("矩阵不是方阵，无法计算它的行列式")
            return 0;
        else:
            cp=self.mat.copy()
            for i in range(self.m):
                temp1=i
                while cp[temp1][i]==0:
                    temp1=temp1+1
                    if temp1==self.m:
                        break
                if temp1==self.m:
                    continue
                switch(cp,i,temp1)
                cancel(cp,self.m,self.n,i,i)
            for i in range(self.m):
                count*=cp[i][i]
        return count

#计算逆矩阵
    def invert(self):
        if self.m!=self.n:
            print("该矩阵不是方阵，没有逆矩阵！")
            return self.mat
        if self.det()==0 :
            print("该矩阵的行列式为零，没有逆矩阵！")
            return self.mat
        emat=[[0 for i in range(self.m)] for i in range(self.m)]
        cp=self.mat.copy()
        for i in range(self.m):
            emat[i][i]=1;
        for i in range(self.m):
            temp1=i;
            while cp[temp1][i]==0:
                temp1=temp1+1
                if temp1==self.m:
                    break
            if temp1==self.m:
                continue
            switch(cp,i,temp1)
            switch(emat,i,temp1)
            cancelall(cp,emat,self.m,self.n,i)

        return emat

#数乘
    def scalar(self,scale):
        cp=self.mat.copy()
        for i in range(self.m):
            for j in range(self.n):
                cp[i][j]=scale*cp[i][j]
        return cp

class MatCal:
    def __init__(self,mat1,mat2):
        self.__mat1=mat1
        self.__mat2=mat2

    def add(self):
        if self.__mat1.m!=self.__mat2.m or self.__mat2!=self.__mat1:
            print("非同型矩阵不能相加！")
            return "Wrong!"
        cp=self.__mat2.mat.copy()
        for i in range(self.__mat2.m):
            for j in range(self.__mat2.n):
                cp[i][j]+=self.__mat1.mat[i][j]
        return cp

    def matmulti(self):
        if self.__mat1.n!=self.__mat2.m:
            print("矩阵一的列不同于矩阵二的行，两矩阵无法相乘！")
            return "Wrong!"
        mul=[[0 for i in range(self.__mat2.n)] for i in range(self.__mat1.m)]
        for i in range(self.__mat1.m):
            for j in range(self.__mat2.n):
                for count in range(self.__mat2.m):
                    mul[i][j]+=self.__mat1.mat[i][count]*self.__mat2.mat[count][j]
        return mul


if __name__ == '__main__':
    size=0
    mats=[]
    while True:
        print("请输入你要做的序号:")
        print("1.加入矩阵")
        print("2.显示所有矩阵")
        print("3.转置矩阵")
        print("4.行列式计算")
        print("5.逆矩阵计算")
        print("6.矩阵相加")
        print("7.矩阵相减")
        print("8.矩阵相乘")
        print("9.退出")
        choice = input("你的选择是：")
        choice = int(choice)
        if choice == 9:
            print("已退出本次计算")
            break
        if choice == 1:
            print("请加入第%d个矩阵"%(size+1))
            print("请输入行数:")
            row=input()
            row=int(row)
            print("请输入列数:")
            volume=input()
            volume=int(volume)
            i=0
            mat=[[0 for i in range(volume)] for i in range(row)]
            while i<row:
                j=0
                while j<volume:
                    print("请输入第%d行第%d列的元素是：" % (i + 1,j + 1))
                    mat[i][j] = int(input())
                    j = j + 1
                i = i + 1
            print("你输入的矩阵是：")
            print(mat)
            matrix=Mat(row,volume,mat)
            mats.append(matrix)
            size=size+1
        if choice == 2:
            for m in mats:
                print(m.mat)

        # cancel(mats[0],3,3,0,0)
        # print(mats[0])
        # switch(mats[0],0,1)
        # print(mats[0])

        if choice == 3:
            print("你要获得第几个矩阵的转置？(上限%d个)："%(size))
            num=int(input())-1
            while num>size:
                print("没有那么多矩阵")
                print("你要获得第几个矩阵的转置？(上限%d个)：" % (size))
                num = int(input())
            print("第%d个矩阵的转置是："%(num+1))
            print(mats[num].trans())

        if choice == 4:
            print("你要获得第几个矩阵的行列式的值？(上限%d个)：" % (size))
            num = int(input()) - 1
            while num > size:
                print("没有那么多矩阵")
                print("你要获得第几个矩阵的行列式得值？(上限%d个)：" % (size))
                num = int(input())
            print("第%d个矩阵的行列式的值是：" % (num + 1))
            print(mats[num].det())

        if choice == 5:
            print("你要获得第几个矩阵的逆矩阵？(上限%d个)：" % (size))
            num = int(input()) - 1
            while num > size:
                print("没有那么多矩阵")
                print("你要获得第几个矩阵的逆矩阵？(上限%d个)：" % (size))
                num = int(input())
            print("第%d个矩阵的逆矩阵是：" % (num + 1))
            print(mats[num].invert())

        if choice == 6:
            if size<2:
                print("矩阵数量不够，请继续加入！")
                continue
            print("请输入要进行相加的两个矩阵的序号(上限%d个)"%(size))
            print("第一个的序号是:")
            num1 = int(input()) - 1
            while num1 > size:
                print("没有那么多矩阵")
                print("第一个的序号是(上限%d个)：" % (size))
                num1 = int(input())
            print("第二个的序号是:")
            num2 = int(input()) - 1
            while num2 > size:
                print("没有那么多矩阵")
                print("第二个的序号是(上限%d个)：" % (size))
                num2 = int(input())
            cal=MatCal(mats[num1],mats[num2])
            print("第%d个矩阵和第%d个矩阵的和是："%(num1+1,num2+1))
            print(cal.add())

        if choice == 7:
            if size<2:
                print("矩阵数量不够，请继续加入！")
                continue
            print("请输入要进行相减的两个矩阵的序号(上限%d个)"%(size))
            print("第一个的序号是:")
            num1 = int(input()) - 1
            while num1 > size:
                print("没有那么多矩阵")
                print("第一个的序号是(上限%d个)：" % (size))
                num1 = int(input())
            print("第二个的序号是:")
            num2 = int(input()) - 1
            while num2 > size:
                print("没有那么多矩阵")
                print("第二个的序号是(上限%d个)：" % (size))
                num2 = int(input())
            cp=mats[num2].mat.copy()
            for i in range(mats[num2].m):
                for j in range(mats[num2].n):
                    cp[i][j]=-cp[i][j]
            temp=Mat(mats[num2].m,mats[num2].n,cp)
            cal=MatCal(mats[num1],temp)
            print("第%d个矩阵和第%d个矩阵的差是："%(num1+1,num2+1))
            print(cal.add())

        if choice == 8:
            if size<2:
                print("矩阵数量不够，请继续加入！")
                continue
            print("请输入要进行相乘的两个矩阵的序号(上限%d个)"%(size))
            print("第一个的序号是:")
            num1 = int(input()) - 1
            while num1 > size:
                print("没有那么多矩阵")
                print("第一个的序号是(上限%d个)：" % (size))
                num1 = int(input())
            print("第二个的序号是:")
            num2 = int(input()) - 1
            while num2 > size:
                print("没有那么多矩阵")
                print("第二个的序号是(上限%d个)：" % (size))
                num2 = int(input())
            cal=MatCal(mats[num1],mats[num2])
            print("第%d个矩阵和第%d个矩阵相乘的矩阵是："%(num1+1,num2+1))
            print(cal.matmulti())

