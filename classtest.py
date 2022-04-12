# class CountTest:
#     def __init__(self,v,h):
#         self.val=v
#         self.incr=h
#     # def __repr__(self):
#     #     return str(self.val)
#     def increase(self)->str:
#         self.val +=self.incr
#
#
#
#
# a=CountTest(1,2)
# # print(a.increase())
# print(a.val)
# print(id(a))
# print(a)
# print(a)
# print(a)

#
# def apply(func,value):
#     return func(value)
#
#
# print(apply(print,2))


def myfunc(*args):
    for i in args:
        print(i,end=' ')
    if args:
        print('\n','without for loop:->   ',args)


def myfunc1(**kwargs):
    for k,v in kwargs.items():
        print(k,v,sep='->',end=' ')



myfunc(*[10,20,30])
myfunc1(name='amit',sex='male',a=10,b=30)