#!/usr/bin/python

a=1
def fin1(x,y):
   return x+y

def fun2(x,y):
   #return x-y
   def fun(x,y):
      print "in fun %d"%(x-y)
   return fun


def result(func,x,y):
   return func(x,y)

a=result(fin1,100,50)
b=result(fun2,10,10)
print b
print b.func_closure
b(10,20)
#a=10
print "a =%d"%a
#fun()
a+=1
print "a after adding 10 id %d"%a
