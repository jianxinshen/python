#TOC
#切片
#迭代
#列表生成式
#生成器
#迭代器*

#切片
L1=range(10)
M=L1[0:5]
print(M)
# 迭代 for a in L
def FindMinandMax(L):
    if L==[]:
        print(None, None)
    else:
        Max=L[0]
        Min=L[0]
        for a in L:
            if a<Min:
                Min=a
            else:
                Max=a
    print("Max=",Max,
          "Min=",Min)

LL=range(10)
FindMinandMax(LL)

#列表生成式 x for a in if
L = ['Hello', 'World', 18, 'Apple', None]
def LowerL(L):
    L2=[s.lower() for s in L if isinstance(s, str)==True]  #True需要大写
    print(L2)
LowerL(L)

# 生成器 g = (x * x for x in range(10))
# 与列表的不同就是把[]改为()

def fib(max):
    a,b,n=0,1,0
    while n<max:
        yield b        #改成print(b)就是普通函数，yield是另一种定义生成器的方法。
        #print(b)
        a,b=b,a+b
        n=n+1
    return 'done!'

for n in fib(5):  #这里需要使用 for来导出数据，并且得不到return值
    print(n)