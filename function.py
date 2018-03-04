def my_abs(x): #必选参数、默认参数、可变参数、关键字参数、命名关键字参数
    if not isinstance(x,(int,float)):
        raise TypeError("错误的数据类型")
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99))


# ABC三组盘子，将A的盘子通过B移动到C的方法，并打印之
# 递归函数
def plant(n,a="A",b='B',c='C'):
    if n==1:
        print(a,'-->',c)
    else:
        plant(n-1,a,c,b)
        plant(1,a,b,c)
        plant(n-1,b,a,c)

print(plant(3))