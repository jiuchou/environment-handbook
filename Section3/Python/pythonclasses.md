# python classes

## 1. class 类型：新式类 vs 经典类

* https://www.cnblogs.com/bigberg/p/7196866.html

### 1.1 定义方式

**Python 2.x中默认都是经典类，只有显式继承了object才是新式类**

**Python 3.x中默认都是新式类，不必显式的继承object**

### 1.2 保持class与type的统一

新式类对象可以直接通过__class__属性获取自身类型：对新式类的实例执行a.__class__与type(a)的结果是一致的，对于旧式类来说就不一样了

### 1.3 对于多重继承的属性搜索顺序不一样

新式类是采用**广度优先搜索**：子类先在自己的所有父类中从左至右查询，如果没有需要的方法或属性,再到本身父类的父类中去查询。

旧式类采用**深度优先搜索**：子类会沿着父类的父类这样的顺序查询，如果都没有，会返回查找另一个父类。

```python
class A():
    def __init__(self):
        pass
    def get_name(self):
        print("name: A")

class B(A):
    def __init__(self):
        pass

class C(A):
    def __init__(self):
        pass
    def get_name(self):
        print("name: C")

class D(B,C):
    def __init__(self):
        pass

fun =  D()
fun.save()

经典类的答案： name: A
新式类的答案： name: C
```

### 1.4 新式类的优点

新式类更符合OOP编程思想，统一了python中的类型机制。

新式类增加了__slots__内置属性, 可以把实例属性的种类锁定到__slots__规定的范围之中。

新式类增加了__getattribute__方法。

新式类采用super()函数类调用父类的 init()等函数



## 2. class 方法



人与人的差距来源于思维的差距。一等人生而知之，二等人见而知之，三等人见而不知。

在接触python很长一段时间之后，听别人提起 `__init__` 和 `__new__` 的概念，第一反应是 `__init__` 是python类的构造器，排查过资料的时候，想法是，根据命名规范，应该能想到平时不可见的 `__new__` 应该是封装到语言中的东西。

## `__init__()`

* 实例化类

## `__new__()`

* 特性
  1. 在类准备将自身实例化时调用
  2. 类的静态方法，即使没有被加上静态方法装饰器

* 派生不可变类型 

  ```python
  class Round2Float(float):
      def __new__(cls, num):
          num = round(num, 2)
          obj = float.__new__(Round2Float, num)
          return obj
  
  f=Round2Float(4.324599)
  print f
  ```

python 获取本机 IP 地址
https://www.cnblogs.com/z-x-y/p/9529930.html

python 获取本机所有 IP 地址
https://www.jb51.net/article/153540.htm

https://blog.csdn.net/qdx411324962/article/details/46924219


# python闭包
https://www.cnblogs.com/s-1314-521/p/9763376.html

